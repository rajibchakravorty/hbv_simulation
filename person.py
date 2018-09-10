"""
Person object
"""
from numpy.random import rand

from temporal_history import TemporalHistory
from states import AdultStates, InfantStates, ChildStates, \
    CURED, DEAD, INFECTED, HEALTHY

ADULT = 'adult'
INFANT = 'infant'
CHILD = 'child'


class Person(object):
    """
    history: TemporalHistory
        Contains the history of health states for an individual
    health_status : string
        See states.py for detail
    birth_year: int
        year of the birth : the start of the simulation year is 0
    is_alive : boolean
        indicates if the person is alive or not
    health_status: string
        stores the most recent health status
    mother : Person
        Stores the mother for the child; None for an adult mother
    person_type : string
        adult/infant/child
    susecptibility_add : float
        adds to the natural probability of being susceptible
    infected_add : float
        adds to the natural probability of being infected
    death_add : float
        adds to the natural probability of being dead
    """

    def __init__(self, heath_status, birth_year=0,
                 mother=None, person_type=ADULT):

        self.history = TemporalHistory()

        self.is_alive = True

        self.birth_year = birth_year

        self.health_status = heath_status

        self.mother = mother

        self.person_type = person_type

        if self.person_type == ADULT:

            self.states = AdultStates()

        elif self.person_type == INFANT:
            self.states = InfantStates()

        elif self.person_type == CHILD:
            self.states = ChildStates()

        self.update_history(birth_year, self.health_status)

        self.susceptibility_add = 0.
        self.infected_add = 0.
        self.death_add = 0.

    def get_next_health_status(self):
        """
        Method to switch health state according to defined
        state transition probability
        Sets the next health status from among possible trajectory
        """

        nxt = self.states.get_next_state(self.health_status)

        if nxt is None:
            return None

        else:

            next_state, next_state_prob = nxt[0], nxt[1]

            if len(next_state) == 1:
                return next_state
            else:
                rand_num = rand()
                start_prob = 0.
                for idx, nxt_st in enumerate(next_state):

                    end_prob = next_state_prob[idx]

                    if end_prob >= rand_num > start_prob:
                        self.health_status = nxt_st
                        break

                    start_prob = end_prob

    def update_history(self, year, health_status):
        """
        Helper method to update the status
        :param year: int
        :param health_status: string
            the new health status
        """
        self.history.update_history(year, health_status)

    def kill(self, year, description=DEAD):
        """
        helper method to invoke "Death" event for an individual
        :param year: int
        :param description: str

        adds the death event to the history
        """
        self.is_alive = False
        self.history.update_history(year, description)

    def get_health_status(self, year):
        """
        helper method to retrieve the health status of an individual
        on a given year
        :param year: int
        :return string; the health status of the individual

        """
        return self.history.retrieve_state(year)

    def change_state(self):
        """
        helper method to update the state transition
        of an infant->child or child->adult
        """

        if self.person_type == ADULT:

            self.states = AdultStates()

        elif self.person_type == INFANT:
            self.states = InfantStates()

        elif self.person_type == CHILD:
            self.states = ChildStates()


class Mother(Person):

    def __init__(self, health_status=HEALTHY):
        super(Mother, self).__init__(health_status, 0, None, ADULT)


class Child(Person):
    """
    Child : inherits from person;
    """

    def __init__(self, mother, health_status=HEALTHY, birth_year=0):
        """

        :param mother: Person, mother of the child
        :param health_status: string
        :param birth_year: int
        """
        super(Child, self).__init__(health_status, birth_year, mother, INFANT)

    def change_state(self):

        """
        Updates the state transition probability
        :return:
        """
        if self.person_type == INFANT:
            self.states = InfantStates()
        else:
            self.states = ChildStates()

    def become_child_or_adult(self, year):

        age = year - self.birth_year

        if 5 >= age > 1:
            self.person_type = CHILD
        if age >= 5:
            self.person_type = ADULT

        self.change_state()




