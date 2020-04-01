import logging

import pendulum
from django.db import models

logger = logging.getLogger(__name__)


class EmployeeQuerySet(models.QuerySet):
    def seniors(self):
        """
        Filtra funcionários que possuem mais de 8 anos de admissão
        :return: queryset
        """
        eight_years_ago = pendulum.now().subtract(years=8)
        logger.info(f"Filtering employees less than: {eight_years_ago}")
        return self.filter(admission_date__lte=eight_years_ago.date())

    def noobs(self):
        """
        Filtra funcionários que possuem menos de 1 ano de admissão
        :return: queryset
        """
        one_year_ago = pendulum.now().subtract(years=1)
        logger.info(f"Filtering employees less than: {one_year_ago}")
        return self.filter(admission_date__gte=one_year_ago.date())

    def _between(self, initial, final):
        """
        Filtra funcionários dentro de um período de data
        :param initial:
        :param final:
        :return: queryset
        """
        lower_limit = pendulum.now().subtract(years=initial)
        higher_limit = pendulum.now().subtract(years=final)
        logger.info(f"Filtering between: {higher_limit} and {lower_limit}")
        return self.filter(admission_date__range=(higher_limit, lower_limit))

    def juniors(self):
        """
        Filtra funcionários que possuem mais de 1 ano e menos de 3
        :return: queryset
        """
        return self._between(1, 3)

    def wannabes(self):
        """
        Filtra funcionários que possuem mais de 3 ano e menos de 8
        :return: queryset
        """
        return self._between(3, 8)
