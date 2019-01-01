"""
Person
======
Any person in the simulation
"""


import numpy as np

from .constants import (MALE_GENDER, FEMALE_GENDER)

class Person(object):

    def __init__(self, birth_year=-1,
                 gender=MALE_GENDER, is_married=False,
                 health_status=dict(),
                 transformation_matrix=dict(),
                 death_year=-1,
                 death_probability=0.2):

        self._birth_year = birth_year
        self._gender = gender
        self._is_married = is_married
        self._health_status = health_status
        self._transformation_matrix = transformation_matrix
        self._death_year = death_year
        self.death_probability = death_probability

    def set_transformation_matrix(self, new_transformation_matrix):

        self._transformation_matrix = new_transformation_matrix

    def get_year_health_status(self, year):

        if not self._health_status.keys():
            return None

        if year in self._health_status.keys():
            return self._health_status[year]
        else:
            return None

    def update_health_status(self, year):

        if self._death_year != -1:
            return

        current_status = self.get_year_health_status(year-1)

        if current_status is None:
            return

        if current_status not in self._transformation_matrix:
            raise AttributeError('No transformation possible from {}'.format(
                current_status))

        transformation = self._transformation_matrix[current_status]

        next_status = transformation.choose_state()

        self._health_status[year] = next_status

    def death_event(self, year):

        random_number = np.random.random()

        if random_number <= self._death_probability:

            self._death_year = year

    def change_marital_status(self, new_status):

        self._is_married = False