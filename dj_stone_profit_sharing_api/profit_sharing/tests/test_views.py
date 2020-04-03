import pytest
from assertpy import assert_that
from django.test import RequestFactory
from profit_sharing.views import ProfitDistributionView


@pytest.mark.django_db
def test_profit_calculation_base_contract(rf: RequestFactory):
    # GIVEN
    view = ProfitDistributionView()
    payload = {"valor_para_distribuir": 1000000}
    request = rf.post("/calculate", data=payload, content_type="application/json")

    # WHEN
    response = view.post(request)

    # THEN
    assert_that(response.data).is_not_none()
    assert_that(response.data).contains_key(
        "participacoes",
        "total_de_funcionarios",
        "total_distribuido",
        "total_disponibilizado",
        "saldo_total_disponibilizado",
    )
    assert_that(response.data["participacoes"]).is_instance_of(list)


@pytest.mark.django_db
def test_profit_calculation(rf: RequestFactory):
    # GIVEN
    view = ProfitDistributionView()
    payload = {"valor_para_distribuir": 1000000}
    request = rf.post("/calculate", data=payload, content_type="application/json")

    # WHEN
    response = view.post(request)

    # THEN
    assert_that(response.data).is_not_none()
    assert_that(response.data).contains_key(
        "participacoes",
        "total_de_funcionarios",
        "total_distribuido",
        "total_disponibilizado",
        "saldo_total_disponibilizado",
    )
    assert_that(response.data["participacoes"]).is_instance_of(list)
