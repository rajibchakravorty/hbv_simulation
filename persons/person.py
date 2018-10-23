

from constants import MALE, FEMALE, HEALTHY
from group import PopulationGroup

class Person(object):

    def __init__(self, birth_year=-1,
                 gender=FEMALE, hbv_status = HEALTHY,
                 group_indicator = 'female'):

        self.gender = gender
        self.birth_year = birth_year
        self.death_year = -1

        self.alive = True

        self.history = dict()

        self.history[0] = hbv_status

        self.group_indicator = group_indicator

    def person_die(self, year):

        self.alive = False
        self.death_year = year

    def update_hbv_status(self, year, new_status):

        self.history[year] = new_status

class Mother(Person):

    def __init__(self, hbv_status=HEALTHY):

        super(Mother, self).__init__(hbv_status)

class Father(Person):

    def __init__(self, hbv_status=HEALTHY):

        super(Father, self).__init__(gender=MALE,
                                     hbv_status=hbv_status)

class Couple(object):

    def __init__(self, mother_hbv_status, father_hbv_status):

        father = Father(father_hbv_status)
        mother = Mother(mother_hbv_status)