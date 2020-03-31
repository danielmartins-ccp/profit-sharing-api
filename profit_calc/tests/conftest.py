import pytest


def user_data_with_expected_profit():
    return [
        (
            {
                "nome": "S[8+] | T[8+]",
                "data_de_admissao": "2000-01-01",
                "salario_bruto": 15000.0,
                "area": "Diretoria",
                "cargo": "Diretor Financeiro",
            },
            216000.0,
        ),
        (
            {
                "nome": "S[8+] | T[3<8]",
                "data_de_admissao": "2015-01-01",
                "salario_bruto": 15000.0,
                "area": "Diretoria",
                "cargo": "Diretor Financeiro",
            },
            144000.0,
        ),
        (
            {
                "nome": "S[8+] | T[1<3]",
                "data_de_admissao": "2019-01-01",
                "salario_bruto": 15000.0,
                "area": "Diretoria",
                "cargo": "Diretor Financeiro",
            },
            108000.0,
        ),
        (
            {
                "nome": "S[8+] | T[<1]",
                "data_de_admissao": "2019-12-01",
                "salario_bruto": 15000.0,
                "area": "Diretoria",
                "cargo": "Diretor Financeiro",
            },
            72000.0,
        ),
        (
            {
                "nome": "S[>5<8] | T[8+]",
                "data_de_admissao": "2010-12-01",
                "salario_bruto": 6270.0,
                "area": "Diretoria",
                "cargo": "Diretor Financeiro",
            },
            150480.0,
        ),
        (
            {
                "nome": "S[>5<8] | T[3<8]",
                "data_de_admissao": "2016-12-01",
                "salario_bruto": 6270.0,
                "area": "Diretoria",
                "cargo": "Diretor Financeiro",
            },
            100320.0,
        ),
        (
            {
                "nome": "S[>5<8] | T[1<3]",
                "data_de_admissao": "2018-12-01",
                "salario_bruto": 6270.0,
                "area": "Diretoria",
                "cargo": "Diretor Financeiro",
            },
            75240.0,
        ),
        (
            {
                "nome": "S[>5<8] | T[<1]",
                "data_de_admissao": "2019-12-01",
                "salario_bruto": 6270.0,
                "area": "Diretoria",
                "cargo": "Diretor Financeiro",
            },
            50160.0,
        ),
        (
            {
                "nome": "S[>3<5] | T[8+]",
                "data_de_admissao": "2010-12-01",
                "salario_bruto": 4180.0,
                "area": "Diretoria",
                "cargo": "Diretor Financeiro",
            },
            150480.0,
        ),
        (
            {
                "nome": "S[>3<5] | T[>3<8]",
                "data_de_admissao": "2015-12-01",
                "salario_bruto": 4180.0,
                "area": "Diretoria",
                "cargo": "Diretor Financeiro",
            },
            100320.0,
        ),
        (
            {
                "nome": "S[>3<5] | T[>1<3]",
                "data_de_admissao": "2018-12-01",
                "salario_bruto": 4180.0,
                "area": "Diretoria",
                "cargo": "Diretor Financeiro",
            },
            75240.0,
        ),
        (
            {
                "nome": "S[>3<5] | T[>1]",
                "data_de_admissao": "2019-12-01",
                "salario_bruto": 4180.0,
                "area": "Diretoria",
                "cargo": "Diretor Financeiro",
            },
            50160.0,
        ),
        (
            {
                "nome": "S[<3] | T[8+]",
                "data_de_admissao": "2010-12-01",
                "salario_bruto": 2090.0,
                "area": "Diretoria",
                "cargo": "Diretor Financeiro",
            },
            150480.0,
        ),
        (
            {
                "nome": "S[<3] | T[>3<8]",
                "data_de_admissao": "2015-12-01",
                "salario_bruto": 2090.0,
                "area": "Diretoria",
                "cargo": "Diretor Financeiro",
            },
            100320.0,
        ),
        (
            {
                "nome": "S[<3] | T[>1<3]",
                "data_de_admissao": "2018-12-01",
                "salario_bruto": 2090.0,
                "area": "Diretoria",
                "cargo": "Diretor Financeiro",
            },
            75240.0,
        ),
        (
            {
                "nome": "S[<3] | T[<1]",
                "data_de_admissao": "2019-12-01",
                "salario_bruto": 2090.0,
                "area": "Diretoria",
                "cargo": "Diretor Financeiro",
            },
            50160.0,
        ),
        (
            {
                "nome": "Trainee | T[8+]",
                "data_de_admissao": "2010-12-01",
                "salario_bruto": 2090.0,
                "area": "Diretoria",
                "cargo": "Estagiario",
            },
            150480.0,
        ),
        (
            {
                "nome": "Trainee | T[>3<8]",
                "data_de_admissao": "2015-12-01",
                "salario_bruto": 2090.0,
                "area": "Diretoria",
                "cargo": "Estagiario",
            },
            100320.0,
        ),
        (
            {
                "nome": "Trainee | T[>1<3]",
                "data_de_admissao": "2018-12-01",
                "salario_bruto": 2090.0,
                "area": "Diretoria",
                "cargo": "Estagiario",
            },
            75240.0,
        ),
        (
            {
                "nome": "Trainee | T[<1]",
                "data_de_admissao": "2019-12-01",
                "salario_bruto": 2090.0,
                "area": "Diretoria",
                "cargo": "Estagiario",
            },
            50160.0,
        ),
    ]


def idfn(fixture_value):
    name = fixture_value[0]["nome"]
    salary = fixture_value[0]["salario_bruto"]
    depart = fixture_value[0]["area"]
    job_title = fixture_value[0]["cargo"]
    admission = fixture_value[0]["data_de_admissao"]
    expected_profit = fixture_value[1]
    return f"{name}+{depart}+{salary}+{job_title}+{admission}={expected_profit}"


@pytest.fixture(params=user_data_with_expected_profit(), ids=idfn)
def users_from_director_board_department(request):
    return request.param[0], request.param[1]
