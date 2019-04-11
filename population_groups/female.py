

from numpy.random import random


from .constants import FEMALE_GENDER, MATERNAL_DEATH_AT_BIRTH
from .person import Person


class Female(Person):

    def __init__(self, birth_year,
                 is_married=False,
                 health_status=dict(),
                 transformation_matrix=dict(),
                 death_probability=0.2,
                 birth_probability=0.2,
                 maternity_death_probability=0.2
                 ):

        super(Female, self).__init__(birth_year=birth_year,
                                     gender=FEMALE_GENDER,
                                     health_status=health_status,
                                     transformation_matrix=transformation_matrix,
                                     is_married=is_married,
                                     death_probability=death_probability)
        self._birth_probability = birth_probability
        self._maternity_death_probability = maternity_death_probability

    def give_birth(self):

        if self.death_year > -1:
            return False

        if not self.is_married:
            return False

        random_number = random()

        if random_number <= self._birth_probability:
            return True
        return False

    def death_at_birth(self):

        if self.death_year > -1:
            return False

        random_number = random()

        if random_number <= self._maternity_death_probability:
            return True

    def year_events(self, year):

        super().year_events(year)

        new_birth = self.give_birth()
        if new_birth:
            #print('Given birth: {}'.format(year))
            if self.death_at_birth():
                self.set_death_status(year, MATERNAL_DEATH_AT_BIRTH)

        return new_birth



