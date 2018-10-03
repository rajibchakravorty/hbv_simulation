"""
Collect statistics over multiple run
"""

import cPickle
import stats

from simulations import simulation_steps

from states import HEALTHY, INFECTED, SUSCEPTIBLE, CURED, DEAD, \
    INFANT_DEATH, CHILD_DEATH, MATERNAL_DEATH, HBV_DEATH


def run_multiples(run_number, years):

    start_run =run_number[0]
    end_run = run_number[1]
    for r in range(start_run, end_run):

        print 'Run {0} started'.format(r)
        m, c = simulation_steps(years)

        with open('mothers_stats_run_{0}.pkl'.format(r), 'wb') as f:
            cPickle.dump(m, f)
        with open('children_stats_run_{0}.pkl'.format(r), 'wb') as f:
            cPickle.dump(c, f)

        print 'Run {0} finished'.format(r)

        break

    return


if __name__ == '__main__':

    start_run = 0 
    end_run = 5
    years = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    run_multiples([start_run, end_run], years)

    mothers = []
    children = []
    for r in range(start_run, end_run):
        with open('mothers_stats_run_{0}.pkl'.format(r), 'rb') as f:
            m = cPickle.load(f)
        with open('childreb_stats_run_{0}.pkl'.format(r), 'rb') as f:
            c = cPickle.load(f)
        mothers.append(m)
        children.append(c)

    mother_status = [HEALTHY, SUSCEPTIBLE, INFECTED, CURED, DEAD, MATERNAL_DEATH]
    child_status = [HEALTHY, SUSCEPTIBLE, INFECTED, CURED, DEAD, INFANT_DEATH, CHILD_DEATH, HBV_DEATH]

    collective_mother_stats = stats.accumulate_collection_stats(mothers, years, mother_status)
    collective_children_stats = stats.accumulate_collection_stats(children, years, child_status)

    with open('mother_stats_multiple.pkl', 'wb') as f:
        cPickle.dump(collective_mother_stats, f)

    with open('children_stats_multiple.pkl', 'wb') as f:
        cPickle.dump(collective_children_stats, f)
