import logging
from decimal import Decimal, ROUND_DOWN
from typing import List

from profit_calc.bags import Weight

logger = logging.getLogger(__name__)


def profit_calculation(
    salary: Decimal, weights: Weight, months: int = 12, rounding: str = ROUND_DOWN
):
    """
    Cálculo de valor máximo de participação considerando um salário base,
    pesos, meses e arredondamento
    :param salary: Salário
    :param weights: Pesos
    :param months: Meses do ano (padrão 12) - pode ser modificado para suportar cálculos menores de 1 ano
    :param rounding: arrendondamento para cima ou para baixo usar módulo decimal
    :return:
    """
    if not isinstance(salary, Decimal):
        logger.info("Convertendo tipo para Decimal")
        salary = Decimal(f"{salary}")
    logger.info(
        f"Cálculo de participação: Salário={salary} + Pesos={weights} + Meses={months} + Rounding{rounding}"
    )
    first_operand = salary * weights.admission_time
    logger.info(f"Salário * PTA = {first_operand}")
    second_operand = salary * weights.department
    logger.info(f"Salário * PAA = {second_operand}")
    third_operand = (first_operand + second_operand) / weights.salary_range
    logger.info(f"Divisão por PFS = {third_operand}")
    final_operation = (third_operand * months).quantize(
        Decimal(".01"), rounding=rounding
    )
    logger.info(f"Multiplicação pelos meses do ano = {final_operation}")
    return final_operation


def proportional_profit_calculation(
    total_amount: Decimal,
    proportional_weight: Weight,
    weights: List[Weight],
    rounding: str = ROUND_DOWN,
):
    """
    Cálculo de divisão diretamente proporcional para um determinado valor
    :param total_amount: Valor total para divisão
    :param proportional_weight: Peso proporcional
    :param weights: Lista de pesos
    :param rounding: Arredondamento
    :return: Valor proporcional para o peso proporcional
    """
    weights_sum = sum([w.total() for w in weights])
    base = (total_amount / weights_sum).quantize(Decimal(".01"), rounding=rounding)
    return base * proportional_weight.total()
