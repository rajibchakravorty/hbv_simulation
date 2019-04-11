"""
Person
======
Any person in the simulation
"""


import numpy as np

from .constants import (MALE_GENDER, DEATH)


class Person(object):

    def __init__(self, birth_year=-1,
                 gender=MALE_GENDER, is_married=False,
                 health_status=dict(),
                 transformation_matrix=dict(),
                 death_probability=0.2,
                 config=None):

        self.birth_year = birth_year
        self.gender = gender
        self.is_married = is_married
        self.health_status = health_status
        self.transformation_matrix = transformation_matrix
        self.death_year = -1
        self.death_probability = death_probability
        self.config = config

    def get_year_health_status(self, year):

        if not self.health_status.keys():
            return None

        if year in self.health_status.keys():
            return self.health_status[year]
        else:
            return None

    def update_health_status(self, year):

        if self.death_year != -1:
            return

        current_status = self.get_year_health_status(year-1)

        if current_status is None:
            return

        if current_status not in self.transformation_matrix:
            raise AttributeError('No transformation possible from {}'.format(
                current_status))

        transformation = self.transformation_matrix[current_status]

        next_status = transformation.choose_state()

        self.health_status[year] = next_status

    def set_death_status(self, year, status=DEATH):

        self.death_year = year
        self.health_status[year] = status

    def death_event(self, year, death_status=DEATH):

        if self.death_year != -1:
            return

        health_status = self.get_year_health_status(year-1)

        random_number = np.random.random()

        if random_number <= self.death_probability[health_status]:

            self.set_death_status(year, death_status)

    def change_marital_status(self, new_status):

        self.is_married = new_status

    def year_events(self, year, death_status=DEATH):

        self.death_event(year, death_status)

        self.update_health_status(year)