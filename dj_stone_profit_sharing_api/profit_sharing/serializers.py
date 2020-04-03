from profit_calc.bags import Weight
from profit_sharing.models import Department, Employee
from rest_framework import fields
from rest_framework.serializers import ModelSerializer, Serializer


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeProfitCaculatedSerializer(ModelSerializer):
    matricula = fields.CharField(source="registration_number")
    nome = fields.CharField(source="name")
    valor_da_participação = fields.SerializerMethodField()

    def __init__(self, instance=None, calculation_weight=None, **kwargs):
        self._weight = calculation_weight or None
        super().__init__(instance, **kwargs)

    class Meta:
        model = Employee
        fields = ["matricula", "nome", "valor_da_participação"]

    def get_valor_da_participação(self, obj: Employee):
        weight = self._weight or Weight(0, 0, 1)
        return obj.profit_calculation(weight)


class ProfitDistributionSerializer(Serializer):
    valor_para_distribuicao = fields.DecimalField(
        max_digits=10, decimal_places=2, source="amount"
    )
