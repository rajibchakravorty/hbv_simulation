"""
Utility function
"""

from numpy.random import rand


def random_less_than(prob):

    rand_num = rand()

    return rand_num < prob


def random_between(small_prob, large_prob):

    rand_num = rand()

    return small_prob < rand_num <= large_prob


def random_greater_than(prob):

    rand_num = rand()

    return rand_num < prob