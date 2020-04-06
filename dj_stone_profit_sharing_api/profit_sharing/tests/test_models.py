from decimal import Decimal

import pytest
from assertpy import assert_that
from model_bakery import baker
from profit_calc.bags import Weight
from profit_calc.specifications import Specification


@pytest.mark.django_db
def test_success_employee_get_weight():
    employee = baker.make_recipe("profit_sharing.director_8y_8s")
    isinstance(employee.get_weight(), Weight)
    assert_that(employee.get_weight()).is_instance_of(Weight)
    assert_that(employee.get_weight()).is_not_equal_to(Weight(0, 0, 1))


@pytest.mark.django_db
def test_failure_employee_get_weight():
    employee = baker.make_recipe("profit_sharing.unknown_8y_8s")
    assert_that(employee.get_weight()).is_instance_of(Weight)
    assert_that(employee.get_weight()).is_equal_to(Weight(0, 0, 1))


@pytest.mark.django_db
def test_success_employee_as_dict_contract():
    employee = baker.make_recipe("profit_sharing.director_8y_8s")
    assert_that(employee.as_dict()).contains_key(
        "nome", "data_de_admissao", "salario_bruto", "area", "cargo"
    )


@pytest.mark.django_db
def test_success_employee_get_specification():
    employee = baker.make_recipe("profit_sharing.director_8y_8s")
    assert_that(employee.get_specification()).is_instance_of(Specification)


@pytest.mark.django_db
def test_failure_employee_get_specification():
    employee = baker.make_recipe("profit_sharing.unknown_8y_8s")
    assert_that(employee.get_specification()).is_none()


@pytest.mark.django_db
def test_success_employee_proportional_profit_calculation():
    employee = baker.make_recipe("profit_sharing.director_8y_8s")
    assert_that(
        employee.proportional_profit_calculation(Decimal("10000.00"), [Weight(2, 3, 5)])
    ).is_not_equal_to(
        employee.profit_calculation
    )  # Não bateu no teto, usou proporcional


@pytest.mark.django_db
def test_employee_proportional_profit_calculation_does_not_go_beyond_the_ceiling():
    employee = baker.make_recipe("profit_sharing.director_8y_8s")
    assert_that(
        employee.proportional_profit_calculation(
            Decimal("1000000.00"), [Weight(2, 3, 5)]
        )
    ).is_equal_to(
        employee.profit_calculation
    )  # Bateu teto, usou limite
