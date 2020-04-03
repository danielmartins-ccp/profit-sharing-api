import pytest

from assertpy import assert_that
from profit_calc.bags import Weight
from profit_calc.calculation import profit_calculation
from profit_calc.specifications import (
    AccountingDepartment,
    AdmissionTimeInYearsBetween,
    AdmissionTimeInYearsGreaterThan,
    AdmissionTimeInYearsLessThan,
    CustomerExperienceDepartment,
    DirectorBoard,
    FacilitiesDepartment,
    FinancialDepartment,
    ITDepartment,
    SalaryBetween,
    SalaryGreaterThan,
    SalaryLessThan,
    Trainee,
)


@pytest.mark.parametrize(
    "specification,department",
    [
        (DirectorBoard(), "Diretoria"),
        (AccountingDepartment(), "Contabilidade"),
        (FinancialDepartment(), "Financeiro"),
        (ITDepartment(), "Tecnologia"),
        (FacilitiesDepartment(), "Serviços Gerais"),
        (CustomerExperienceDepartment(), "Relacionamento com o cliente"),
    ],
)
def test_success_department_specs(specification, department):
    user_data = {"area": department}
    assert_that(specification.is_satisfied_by(user_data)).is_true()


@pytest.mark.parametrize(
    "specification,department",
    [
        (DirectorBoard(), "NOT Diretoria"),
        (AccountingDepartment(), "NOT Contabilidade"),
        (FinancialDepartment(), "NOT Financeiro"),
        (ITDepartment(), "NOT Tecnologia"),
        (FacilitiesDepartment(), "NOT Serviços Gerais"),
        (CustomerExperienceDepartment(), "NOT Relacionamento com o cliente"),
    ],
)
def test_fail_director_department(specification, department):
    user_data = {"area": department}
    assert_that(specification.is_satisfied_by(user_data)).is_false()


@pytest.mark.parametrize(
    "specification,salary,expected",
    [
        (SalaryGreaterThan(5), 5226.0, True),
        (SalaryGreaterThan(5), 5225.0, False),
        (SalaryGreaterThan(5), 4526.0, False),
    ],
)
def test_salary_above_spec(specification, salary, expected):
    user_data = {"salario_bruto": salary}
    assert_that(specification.is_satisfied_by(user_data)).is_equal_to(expected)


@pytest.mark.parametrize(
    "specification,salary,expected",
    [
        (SalaryLessThan(8), 10000.0, False),
        (SalaryLessThan(8), 5000.0, True),
        (SalaryLessThan(8), 8360.0, False),
    ],
)
def test_salary_below_spec(specification, salary, expected):
    user_data = {"salario_bruto": salary}
    assert_that(specification.is_satisfied_by(user_data)).is_equal_to(expected)


@pytest.mark.parametrize(
    "specification,salary,expected",
    [
        (SalaryBetween(5, 8), 6000.0, True),
        (SalaryBetween(1, 3), 8360.9, False),
        (SalaryBetween(2, 3), 2090.0, True),
        (SalaryBetween(2, 3), 2091.0, True),
        (SalaryBetween(2, 3), 3135.0, True),
        (SalaryBetween(2, 3), 3136.0, False),
    ],
)
def test_salary_between_spec(specification, salary, expected):
    user_data = {"salario_bruto": salary}
    assert_that(specification.is_satisfied_by(user_data)).is_equal_to(expected)


@pytest.mark.parametrize(
    "specification,admission_time,expected",
    [
        (
            AdmissionTimeInYearsLessThan(1, current_time="2020-01-01"),
            "2015-01-05",
            False,
        ),
        (
            AdmissionTimeInYearsLessThan(1, current_time="2020-01-01"),
            "2019-01-05",
            True,
        ),
    ],
)
def test_admission_time_year_below_spec(specification, admission_time, expected):
    user_data = {"data_de_admissao": admission_time}
    assert_that(specification.is_satisfied_by(user_data)).is_equal_to(expected)


@pytest.mark.parametrize(
    "specification,admission_time,expected",
    [
        (
            AdmissionTimeInYearsBetween(1, 3, current_time="2020-01-01"),
            "2018-01-01",
            True,
        ),
        (
            AdmissionTimeInYearsBetween(1, 3, current_time="2020-01-01"),
            "2015-01-01",
            False,
        ),
        (
            AdmissionTimeInYearsBetween(1, 3, current_time="2020-01-01"),
            "2019-12-10",
            False,
        ),
    ],
)
def test_admission_time_year_between_spec(specification, admission_time, expected):
    user_data = {"data_de_admissao": admission_time}
    assert_that(specification.is_satisfied_by(user_data)).is_equal_to(expected)


@pytest.mark.parametrize(
    "specification,admission_time,expected",
    [
        (
            AdmissionTimeInYearsGreaterThan(5, current_time="2020-01-01"),
            "2018-01-01",
            False,
        ),
        (
            AdmissionTimeInYearsGreaterThan(5, current_time="2020-01-01"),
            "2010-01-01",
            True,
        ),
    ],
)
def test_admission_time_year_above_spec(specification, admission_time, expected):
    user_data = {"data_de_admissao": admission_time}
    assert_that(specification.is_satisfied_by(user_data)).is_equal_to(expected)


def test_profit_calculation(users_from_director_board_department):
    board_rules = {
        DirectorBoard()
        & SalaryGreaterThan(8)
        & AdmissionTimeInYearsGreaterThan(8): Weight(5, 1, 5,),
        DirectorBoard()
        & SalaryGreaterThan(8)
        & AdmissionTimeInYearsLessThan(1): Weight(1, 1, 5),
        DirectorBoard()
        & SalaryGreaterThan(8)
        & AdmissionTimeInYearsBetween(3, 8): Weight(3, 1, 5),
        DirectorBoard()
        & SalaryGreaterThan(8)
        & AdmissionTimeInYearsBetween(1, 3): Weight(2, 1, 5),
        DirectorBoard()
        & SalaryBetween(5, 8)
        & AdmissionTimeInYearsGreaterThan(8): Weight(5, 1, 3),
        DirectorBoard()
        & SalaryBetween(5, 8)
        & AdmissionTimeInYearsBetween(3, 8): Weight(3, 1, 3),
        DirectorBoard()
        & SalaryBetween(5, 8)
        & AdmissionTimeInYearsBetween(1, 3): Weight(2, 1, 3),
        DirectorBoard()
        & SalaryBetween(5, 8)
        & AdmissionTimeInYearsLessThan(1): Weight(1, 1, 3),
        DirectorBoard()
        & SalaryBetween(3, 5)
        & AdmissionTimeInYearsGreaterThan(8): Weight(5, 1, 2),
        DirectorBoard()
        & SalaryBetween(3, 5)
        & AdmissionTimeInYearsBetween(3, 8): Weight(3, 1, 2),
        DirectorBoard()
        & SalaryBetween(3, 5)
        & AdmissionTimeInYearsBetween(1, 3): Weight(1, 1, 2),
        DirectorBoard()
        & SalaryLessThan(3)
        & AdmissionTimeInYearsGreaterThan(8): Weight(5, 1, 1),
        DirectorBoard()
        & SalaryLessThan(3)
        & AdmissionTimeInYearsBetween(3, 8): Weight(3, 1, 1),
        DirectorBoard()
        & SalaryLessThan(3)
        & AdmissionTimeInYearsBetween(1, 3): Weight(2, 1, 1),
        DirectorBoard()
        & (Trainee() | SalaryLessThan(3))
        & AdmissionTimeInYearsLessThan(1): Weight(1, 1, 1),
    }

    user_data, expected_profit = users_from_director_board_department

    for specification, weights in board_rules.items():
        if specification.is_satisfied_by(user_data):
            assert_that(
                profit_calculation(user_data["salario_bruto"], weights)
            ).is_equal_to(expected_profit)
