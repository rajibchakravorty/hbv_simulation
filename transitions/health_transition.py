

import numpy as np
from random import shuffle, randint

from population_groups import HEALTHY, SUSCEPTIBLE, INFECTED, CURED



class HealthTransformation():

    def __init__(self, name, transformation_probabilities):
        """
        :param name: Name of the Health Status
        :param transformation_probabilities: Transformation probabilities
        :type transformation_probabilities: dict
        """
        self.name = name
        self.transformation_probabilities = transformation_probabilities

        probabilities = np.array(
            [transformation_probabilities[key] for key in self.transformation_probabilities])

        assert np.sum(probabilities) == 1.

        self.bin_content = list()

        for key in self.transformation_probabilities.keys():

            transformation_probability = self.transformation_probabilities[key]

            number_of_items = int(100. * transformation_probability)

            if number_of_items == 0:
                continue

            self.bin_content.extend([key] * number_of_items)

        shuffle(self.bin_content)

    def choose_state(self):

        max_index = len(self.bin_content) - 1

        chosen_index = randint(0, max_index)

        return self.bin_content[chosen_index]

    def __str__(self):

        transformation_string = 'Transformation probabilities\n'
        transformation_string += str(self.transformation_probabilities)
        transformation_string += '\n'

        status_counts = {HEALTHY: 0,
                         SUSCEPTIBLE: 0,
                         INFECTED: 0,
                         CURED: 0}

        for content in self.bin_content:

            status_counts[content] += 1

        transformation_string += 'Bin Counts\n'
        transformation_string += str(status_counts)

        return transformation_string


