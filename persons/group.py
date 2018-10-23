

import numpy as np
from persons import HEALTHY, SUSCEPTIBLE, INFECTED, CURED

class PopulationGroup(object):

    def __init__(self, state_transition_matrix,
                 hbv_prevelance, hbv_exposure,
                 birth_probability, death_probability,
                 vaccinaton_rate, add_infection_probability,

                 transition_matrix_row_dict = None):

        self.state_transition_matrix = state_transition_matrix
        if transition_matrix_row_dict is None
            self.transition_matrix_row_dict = [HEALTHY, SUSCEPTIBLE,
                                               INFECTED, CURED]
        else:
            self.transition_matrix_row_dict = transition_matrix_row_dict

    def calculate_next_state_probabilities(self,
                                           current_state_probability):

        next_state_probabilities = np.matmul(self.state_transition_matrix,
                                             current_state_probability)
        return next_state_probabilities

    def decide_next_state(self, current_state_probability):

        next_state_probabilities = self.calculate_next_state_probabilities(
            current_state_probability
        )

        maximum_probability_loc = np.argmax(next_state_probabilities)
        return self.transition_matrix_row_dict[maximum_probability_loc]

