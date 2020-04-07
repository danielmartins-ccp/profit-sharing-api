import pytest
from assertpy import assert_that
from model_bakery import baker
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
def test_profit_calculation_ceiling(api_rf):
    # GIVEN
    baker.make_recipe("profit_sharing.director_8y_8s", raw_salary=12696.20)
    view = ProfitDistributionView().as_view()
    payload = {"valor_para_distribuicao": "1000000.00"}
    request = api_rf.post("/calculate", data=payload, format="json")

    # WHEN
    response = view(request)

    # THEN
    assert_that(response.data).is_not_none()
    assert_that(response.data).has_total_de_funcionarios(1)
    assert_that(response.data).has_total_disponibilizado("1000000.00")
    assert_that(response.data).has_total_distribuido("182825.28")
    assert_that(response.data).has_saldo_total_disponibilizado("817174.72")


@pytest.mark.django_db
def test_profit_proportional_calculation(api_rf):
    # GIVEN
    baker.make_recipe("profit_sharing.director_8y_8s", raw_salary=12696.20, _quantity=3)
    view = ProfitDistributionView().as_view()
    payload = {"valor_para_distribuicao": "100000.00"}
    request = api_rf.post("/calculate", data=payload, format="json")

    # WHEN
    response = view(request)

    # THEN
    assert_that(response.data).is_not_none()
    assert_that(response.data).has_total_de_funcionarios(3)
    assert_that(response.data["participacoes"]).extracting(
        "valor_da_participação"
    ).is_equal_to(["33333.30", "33333.30", "33333.30"])
    assert_that(response.data).has_total_disponibilizado("100000.00")
    assert_that(response.data).has_total_distribuido(
        "99999.90"
    )  # Estamos arredondando dizimas para baixo, para não extrapolar valor
    assert_that(response.data).has_saldo_total_disponibilizado("0.10")


@pytest.mark.django_db
def test_profit_calculation_eq_zero_if_no_specification_is_matched(api_rf):
    # GIVEN
    baker.make_recipe("profit_sharing.unknown_8y_8s", raw_salary=12696.20, _quantity=3)
    view = ProfitDistributionView().as_view()
    payload = {"valor_para_distribuicao": "100000.00"}
    request = api_rf.post("/calculate", data=payload, format="json")

    # WHEN
    response = view(request)

    # THEN
    assert_that(response.data).is_not_none()
    assert_that(response.data).has_total_de_funcionarios(3)
    assert_that(response.data["participacoes"]).extracting(
        "valor_da_participação"
    ).is_equal_to(["0.00", "0.00", "0.00"])
    assert_that(response.data).has_total_disponibilizado("100000.00")
    assert_that(response.data).has_total_distribuido(
        "0.00"
    )  # Estamos arredondando dizimas para baixo, para não extrapolar valor
    assert_that(response.data).has_saldo_total_disponibilizado("100000.00")
