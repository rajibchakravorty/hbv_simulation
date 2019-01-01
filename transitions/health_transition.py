

import numpy as np
from random import shuffle, randint


class HealthTransformation():

    def __init__(self, name, transformation_probabilities):
        """
        :param name: Name of the Health Status
        :param transformation_probabilities: Transformation probabilities
        :type transformation_probabilities: dict
        """
        self._name = name
        self._transformation_probabilities = transformation_probabilities

        probabilities = np.array(
            [transformation_probabilities[key] for key in self._transformation_probabilities])

        assert np.sum(probabilities) == 1.

        self.bin_content = list()

        for key in self._trasformation_probabilities.keys():

            transformation_probability = self._transformation_probabilities[key]

            number_of_items = int(100. * transformation_probability)

            if number_of_items == 0:
                continue

            self.bin_content.extend([key] * number_of_items)

        shuffle(self.bin_content)

    def choose_state(self):

        max_index = len(self.bin_content) - 1

        chosen_index = randint(0, max_index)

        return chosen_index
