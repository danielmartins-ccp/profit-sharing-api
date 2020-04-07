import pendulum
from model_bakery.recipe import Recipe, foreign_key
from profit_calc.specifications import BaseSalaryCalculatorMixin
from profit_sharing.models import Department, Employee

board_depart = Recipe(Department, name="Diretoria")
accounting_depart = Recipe(Department, name="Contabilidade")
financial_depart = Recipe(Department, name="Financeiro")
it_depart = Recipe(Department, name="Tecnologia")
facilities_depart = Recipe(Department, name="Serviços Gerais")
customer_depart = Recipe(Department, name="Relacionamento com o cliente")
unknown_depart = Recipe(Department, name="Departamento Desconhecido")


def subtract_years(how_many: int):
    def wrap():
        return pendulum.now().subtract(years=how_many)

    return wrap


def salary(how_many: int):
    def wrap():
        return BaseSalaryCalculatorMixin.BASE_SALARY * how_many

    return wrap


director_8y_8s = Recipe(
    Employee,
    department=foreign_key(board_depart),
    admission_date=subtract_years(9),
    raw_salary=salary(9),
)


unknown_8y_8s = Recipe(
    Employee,
    department=foreign_key(unknown_depart),
    admission_date=subtract_years(9),
    raw_salary=salary(9),
)
