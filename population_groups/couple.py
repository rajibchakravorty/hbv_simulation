

import numpy as np

from .constants import (MALE_GENDER, FEMALE_GENDER,
                        HEALTHY, SUSCEPTIBLE, INFECTED, CURED)
from .child import Child, new_child_birth


class Couple(object):

    def __init__(self, mother, father, config, transformations):

        self.mother = mother
        self.father = father

        self.mother.is_married = True
        self.father.is_married = True

        self.children = list()

        self.config = config
        self.transformations = transformations

    def add_child(self, year):

        mothers_health_status = self.mother.get_year_health_status(year)

        new_child = new_child_birth(birth_year=year,
                                    transformation_matrix=
                                    self.transformations.infant_transition_matrix,
                                    vaccination_probability=self.config.NEWBORN_VACCINATION_RATE,
                                    neonatal_mortality=self.config.NEONATAL_MORTALITY_RATE,
                                    death_probability=self.config.INFANT_MORTALITY_RATE,
                                    max_vaccination_year=self.config.MAX_VACCINATION_YEAR,
                                    mother_health=mothers_health_status
                                    )

        self.children.append(new_child)

    def year_events(self, year):

        #print(type(self.children))

        self.father.year_events(year)
        new_birth = self.mother.year_events(year)

        for c in self.children:

            c.year_events(year)
            age = year - c.birth_year

            if 1 < age < 5:
                c.update_transformation_matrix(self.transformations.child_transition_matrix)

                if c.gender == FEMALE_GENDER:
                    c.update_death_probability(self.config.CHILD_MORTALITY_RATE)
                else:
                    c.update_death_probability(self.config.CHILD_MORTALITY_RATE)

            elif 5 < age:
                if c.gender == FEMALE_GENDER:
                    c.update_death_probability(self.config.FEMALE_MORTALITY_RATE)
                else:
                    c.update_death_probability(self.config.MALE_MORTALITY_RATE)

        if new_birth:
            self.add_child(year)

    def count_children(self):

        return len(self.children)

    def count_children_at_year(self, year):

        count = 0
        for children in self.children:

            if children.death_year != -1:
                count += 1

        return count
