"""
Store and update the health status every year
"""


class TemporalHistory(object):

    def __init__(self):

        self.history = dict()

    def update_history(self, year, state):

        self.history[year] = state

    def retrieve_state(self, year):

        if year in self.history.keys():

            return self.history[year]
        else:
            None

    def get_history(self):

        return self.history
