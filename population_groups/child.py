
import numpy as np

from .constants import (MALE_GENDER, CURED, FEMALE_GENDER,
                        HEALTHY, SUSCEPTIBLE, INFECTED, CURED, NEONATAL_DEATH,
                        INFANT_DEATH, CHILD_DEATH, DEATH)
from .person import Person


def new_child_birth(birth_year,
                    transformation_matrix=dict(),
                    vaccination_probability=dict(),
                    neonatal_mortality=0.02,
                    death_probability=dict(),
                    max_vaccination_year=1e4,
                    mother_health=None):

    new_born_health = dict()
    new_born_health[birth_year] = HEALTHY
    if mother_health is None:
        new_born_health[birth_year] = HEALTHY
    elif mother_health == INFECTED:
        new_born_health[birth_year] = INFECTED

    #set the child gender
    child_gender = MALE_GENDER
    if np.random.random() >= 0.5:
        child_gender = FEMALE_GENDER

    child_vaccination_probability = vaccination_probability[child_gender]

    child = Child(birth_year=birth_year,
                  gender=child_gender,
                  health_status=new_born_health,
                  transformation_matrix=transformation_matrix,
                  death_probability=death_probability,
                  vaccination_probability=child_vaccination_probability,
                  max_vaccination_year=max_vaccination_year)

    random_number = np.random.random()
    #print(neonatal_mortality)
    #print(type(neonatal_mortality))

    if random_number <= neonatal_mortality[child.get_year_health_status(birth_year)]:

        child.set_death_status(birth_year, NEONATAL_DEATH)

    if child.death_year == -1 and child.get_year_health_status(birth_year) != INFECTED:
        random_number = np.random.random()

        if random_number <= child.vaccination_probability:
            child.vaccination_year = birth_year
            child.health_status[birth_year] = CURED

    return child


class Child(Person):

    def __init__(self, birth_year,
                 gender=MALE_GENDER,
                 health_status=dict(),
                 transformation_matrix=dict(),
                 death_probability=dict(),
                 vaccination_probability=0.8,
                 max_vaccination_year=1e4):

        super(Child, self).__init__(birth_year=birth_year,
                                    gender=gender,
                                    is_married=False,
                                    health_status=health_status,
                                    transformation_matrix=transformation_matrix,
                                    death_probability=death_probability)

        self.vaccination_probability = vaccination_probability
        self.max_vaccination_year = max_vaccination_year
        self.vaccination_year = -1

    def update_death_probability(self, new_probability):

        if self.death_year != -1:
            return

        self.death_probability = new_probability

    def update_transformation_matrix(self, new_transformation_matrix):

        self.transformation_matrix = new_transformation_matrix

    def get_vaccination(self, year):

        if self.death_year != -1:
            return False

        if year >= self.max_vaccination_year:
            return False

        if self.get_year_health_status(year=year-1) == INFECTED:
            return False

        if self.vaccination_year >= 0:
            return True

        else:

            random_number = np.random.random()

            if random_number <= self.vaccination_probability:
                self.vaccination_year = year
                self.health_status[year] = CURED
                return True

    @override
    def death_event(self, year, death_status=INFANT_DEATH):

        if self.death_year != -1:
            return

        health_status = self.get_year_health_status(year-1)

        random_number = np.random.random()

        if random_number <= self.death_probability[health_status]:

            if year-self.birth_year <= 1:
                self.set_death_status(year, INFANT_DEATH)
            elif 1 < year-self.birth_year < 5:
                self.set_death_status(year, CHILD_DEATH)
            else:
                self.set_death_status(year)

    def year_events(self, year, ):

        super().year_events(year)

        self.get_vaccination(year)




