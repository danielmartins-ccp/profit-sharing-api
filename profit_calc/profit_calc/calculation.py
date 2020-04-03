import logging

from profit_calc.bags import Weight

logger = logging.getLogger(__name__)


def profit_calculation(salary: float, weights: Weight):
    logger.info(f"Profit calculation W:{weights}")
    first_operand = salary * weights.admission_time
    logger.info(f"First operand: {first_operand}")
    second_operand = salary * weights.department
    logger.info(f"Second operand: {second_operand}")
    third_operand = (first_operand + second_operand) / weights.salary_range
    logger.info(f"Third operand: {third_operand}")
    return third_operand * 12
