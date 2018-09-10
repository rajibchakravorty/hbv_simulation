"""
Various methods for actions on Children/Infants (0-5 years)
"""
from person import Child

from utility import random_less_than

from states import HEALTHY

from states import INFECTED, SUSCEPTIBLE

import constants


def create_child(health_status, mother, birth_year):
    """
    Factory method to create Child person
    :param health_status: string. see states.py for details
    :param mother: Adult mother of the child
    :param birth_year: int; year of the birth
    :return:
        Child
    """
    child = Child(health_status=health_status, mother=mother,
                  birth_year=birth_year)

    ## check if child is naturally dead
    if is_neonatal_dead():
        child.kill(birth_year)
        return child

    ## if alive, see if the mother is infected
    if is_neonatal_infected(child, mother):
        child.health_status = INFECTED
        child.update_history(birth_year, health_status=child.health_status)

    ## if not infected, see if susceptible
    else:
        if is_neonatal_susceptible():
            child.health_status = SUSCEPTIBLE
            child.update_history(birth_year, health_status=child.health_status)

    if is_neonatal_vaccinated():
        child.health_status = HEALTHY
        child.update_history(birth_year, health_status=HEALTHY)

    return child


def is_neonatal_dead():
    """
    Action to decide if the infant is dead upon birth
    Returns:
        Boolean
    """
    return random_less_than(constants.NEONATAL_MORTALITY_RATE)


def is_infant_dead(add_prob=0.):
    """
    Action to decide if the infant dies
    :param add_prob: float; any additional porobability over natural probability
    :return:
        boolean
    """
    return random_less_than(constants.INFANT_MORTALITY_RATE+add_prob)


def is_child_dead(add_prob=0.):
    """
    Action to decide if the child dies
    :param add_prob: float; any additional porobability over natural probability
    :return:
        boolean
    """
    return random_less_than(constants.CHILD_MORTALITY_RATE+add_prob)


def is_neonatal_infected(child, mother):
    """
    Action to decide if the infant is infected due to mother being infected
    :param child: Person; the child
    :param mother: Person; the mother of the child
    :return:
        boolean
    """
    mothers_health_status = mother.get_health_status(child.birth_year)

    return mothers_health_status == INFECTED


def is_neonatal_susceptible():
    """
    Action to decide if the infant is exposed and susceptible
    :return:
        boolean
    """
    return random_less_than(constants.INFANT_EXPOSURE_RATE)


def is_infant_susceptible():
    """
    Action to decide if the infant is exposed and susceptible
    :return:
        boolean
    """
    return random_less_than(constants.INFANT_EXPOSURE_RATE)


def is_child_susceptible():
    """
    Action to decide if the child is exposed and susceptible
    :return:
        boolean
    """
    return random_less_than(constants.CHILD_EXPOSURE_RATE)


def is_neonatal_vaccinated():
    """
    Action to decide if the infant is vaccinated
    :return:
        boolean
    """
    return random_less_than(constants.VACCINATION_RATE)