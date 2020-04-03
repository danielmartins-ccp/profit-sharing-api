import pytest
from assertpy import assert_that
from profit_sharing.views import ProfitDistributionView


@pytest.mark.django_db
def test_profit_calculation_base_contract(api_rf):
    # GIVEN
    view = ProfitDistributionView().as_view()
    payload = {"valor_para_distribuicao": 1000000.00}
    request = api_rf.post("/calculate", data=payload, format="json")

    # WHEN
    response = view(request)

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
def test_profit_calculation(api_rf):
    # GIVEN
    view = ProfitDistributionView().as_view()
    payload = {"valor_para_distribuicao": 1000000.00}
    request = api_rf.post("/calculate", data=payload, format="json")

    # WHEN
    response = view(request)

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
