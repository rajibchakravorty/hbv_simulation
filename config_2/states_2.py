
from constants_2 import SUSCEPTIBLE, HEALTHY, CURED, INFECTED


class States(object):

    def __init__(self, next_status=None):

        self.states = [SUSCEPTIBLE, CURED, HEALTHY, INFECTED]

        self.next_states = next_status

    def get_next_state(self, current_state):

        return self.next_states[current_state]


class AdultStates(States):

    def __init__(self):

        # this defines the transition matrix among 4 states
        # for each state, the next states is a list of next
        # possible states and a list of cumulative probabilities

        next_status = dict()
        # if healthy - it always stays healthy with probability = 1
        next_status[HEALTHY] = ([HEALTHY], [1.0])
        # if susceptible,
        # stays susceptible with probability 0.8
        # converts to infected with probability 1.0-0.8=0.2
        next_status[SUSCEPTIBLE] = ([SUSCEPTIBLE, INFECTED], [0.8, 1.0])
        # if infected,
        # stays infected with probability 0.2
        # converts to cured with probability 1.0-0.2=0.8
        next_status[INFECTED] = ([INFECTED, CURED], [0.2, 1.0])
        # once cured,
        # stays cured with probability 1.0
        next_status[CURED] = ([CURED], [1.0])

        super(AdultStates, self).__init__(next_status)


class InfantStates(States):

    def __init__(self):

        next_status = dict()
        next_status[HEALTHY] = ([HEALTHY], [1.0])
        next_status[SUSCEPTIBLE] = ([SUSCEPTIBLE, INFECTED], [0.6, 1.0])
        next_status[INFECTED] = ([INFECTED, CURED], [0.99, 1.0])
        next_status[CURED] = ([CURED], [1.0])

        super(InfantStates, self).__init__(next_status)


class ChildStates(States):

    def __init__(self):

        next_status = dict()
        next_status[HEALTHY] = ([HEALTHY], [1.0])
        next_status[SUSCEPTIBLE] = ([SUSCEPTIBLE, INFECTED], [0.8, 1.0])
        next_status[INFECTED] = ([INFECTED, CURED], [0.9, 1.0])
        next_status[CURED] = ([CURED], [1.0])

        super(ChildStates, self).__init__(next_status)
