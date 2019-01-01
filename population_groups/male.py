

from .constants import MALE_GENDER
from .person import Person


class Male(Person):

    def __init__(self, birth_year=-1,
                 is_married=False,
                 health_status=dict(),
                 transformation_matrix=dict(),
                 death_year=-1,
                 death_probability=0.2):

        super(Male, self).__init__(birth_year=birth_year,
                                   gender=MALE_GENDER,
                                   is_married=is_married,
                                   health_status=health_status,
                                   transformation_matrix=transformation_matrix,
                                   death_year=death_year,
                                   death_probability=death_probability)