"""
Collect statistics over multiple run
"""

import cPickle
import stats
from os.path import join

from configuration import constants

HEALTHY = constants.HEALTHY
INFECTED = constants.INFECTED
SUSCEPTIBLE = constants.SUSCEPTIBLE
CURED = constants.CURED
DEAD = constants.DEAD
INFANT_DEATH = constants.INFANT_DEATH
CHILD_DEATH = constants.CHILD_DEATH
HBV_DEATH = constants.HBV_DEATH

import configuration.constants as constants

def collect_stats(folder, collection_status, years,
                  outfile, end_run=0, is_mother=True):

    collective_stats = dict()

    for st in collection_status:
        year_states = dict()
        for year in years:
            year_states[year] = [0]
        collective_stats[st] = year_states

    if is_mother:
        file_prefix = 'mothers_stats_run'
    else:
        file_prefix = 'children_stats_run'

    for r in range(0, end_run):
        print(folder)
        print 'Reading {0}_{1}.pkl'.format(file_prefix, r)
        with open(join(folder, '{0}_{1}.pkl'.format(file_prefix, r)), 'rb') as f:
            collection = cPickle.load(f)

        run_stat = stats.yearly_collection_stats(collection, years, collection_status)

        for st in collection_status:
            year_states = run_stat[st]
            for year in years:
                collective_stats[st][year].append(year_states[year])
        del run_stat

    with open(outfile, 'wb') as f:
        cPickle.dump(collective_stats, f)

    return


if __name__ == '__main__':

    folder = constants.output_folder_prefix
    years = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    child_status = [HEALTHY, SUSCEPTIBLE, INFECTED, CURED, DEAD, INFANT_DEATH, CHILD_DEATH, HBV_DEATH]
    outfile = join(folder, 'collective_mother_stats.pkl')
    collect_stats(folder, child_status, years, outfile, 10, False)
