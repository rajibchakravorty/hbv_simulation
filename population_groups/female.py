

from .constants import FEMALE_GENDER
from .person import Person


class Female(Person):

    def __init__(self, birth_year,
                 is_married=False,
                 health_status=dict(),
                 transformation_matrix=dict(),
                 death_year=-1,
                 death_probability=0.2
                 ):

        super(Female, self).__init__(birth_year=birth_year,
                                     gender=FEMALE_GENDER,
                                     health_status=health_status,
                                     transformation_matrix=transformation_matrix,
                                     is_married=is_married,
                                     death_year=death_year,
                                     death_probability=death_probability)

    def give_birth(self, birth_probability):

        