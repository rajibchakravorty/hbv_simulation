"""
Various methods for actions on Adults
"""

from person import Mother

import constants

from utility import random_less_than

from states import HEALTHY


def _create_mother(health_status=HEALTHY):
    """
    Private Factory method to create a "mother"

    health_status: string
        See states.py for details; Defaults to Healthy

    Returns
    Mother
        A Person Object as an Adult
    """
    m = Mother(health_status=health_status)

    return m


def initialize_mothers(population_distribution):
    """
    Creates a population of mothers

    population_distribution: dict
        Dict with member number of each of the health state keys

    Returns
    list:
        Of mothers
    """

    mothers = list()

    for key in population_distribution.keys():
        number = population_distribution[key]
        for _ in range(number):

            mothers.append(_create_mother(health_status=key))

    return mothers


def is_adult_dead():
    """
    Action for any adult to decide if an adult is dead
    Returne:
        Boolean
    """
    return random_less_than(constants.ADULT_MORTALITY_RATE)


def is_mother_giving_birth():
    """
    Action for a mother to decide if she is giving birth in that year
    Returns:
        Boolean
    """
    return random_less_than(constants.BIRTH_PROB)


def is_mother_dead_at_birth():
    """
    Action to decide if the mother dies of child birth
    Returns:
        Boolean
    """
    return random_less_than(constants.MATERNAL_MORTALITY_RATE)