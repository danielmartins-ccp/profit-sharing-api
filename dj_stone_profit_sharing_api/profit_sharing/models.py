import logging

from django.db import models
from profit_calc.bags import Weight
from profit_calc.calculation import profit_calculation, proportional_profit_calculation
from profit_sharing.managers import EmployeeQuerySet
from profit_sharing.specifications import specifications

logger = logging.getLogger(__name__)


class Timestampable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Department(Timestampable, models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


class Employee(Timestampable, models.Model):
    registration_number = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    raw_salary = models.DecimalField(max_digits=10, decimal_places=2)
    admission_date = models.DateField()
    people = EmployeeQuerySet.as_manager()

    def __str__(self):
        return f"[{self.registration_number}] {self.name}"

    def as_dict(self):
        return {
            "nome": self.name,
            "data_de_admissao": self.admission_date.isoformat(),
            "salario_bruto": float(self.raw_salary),
            "area": self.department.name,
            "cargo": self.position,
        }

    def get_specification(self):
        for spec, weights in specifications.items():
            if spec.is_satisfied_by(self.as_dict()):
                logger.debug("Matched a specification of weights")
                return spec

    def get_weight(self):
        """
        Busca os pesos configurados para a specificação que este
        usuário encaixa.
        No caso de não bater nenhuma especificação, retorna um peso zerado.
        :return: weight
        """
        try:
            return specifications[self.get_specification()]
        except KeyError:
            logger.warning("Can't find specification for {self}")
            return Weight(0, 0, 1)

    @property
    def profit_calculation(self):
        return profit_calculation(self.raw_salary, self.get_weight())

    def proportional_profit_calculation(self, total_amount, total_weights):
        """
        Retorna cálculo proporcional ao valor alvo ou o limite de participação
        para não extrapolar.
        :param total_amount: Total a ser distribuido
        :param total_weights: Total de pesos para o calculo proporcional
        :return: profit_calculation
        """
        proportional = proportional_profit_calculation(
            total_amount, self.get_weight(), total_weights
        )
        return (
            proportional
            if proportional <= self.profit_calculation
            else self.profit_calculation
        )
