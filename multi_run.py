"""
Collect statistics over multiple run
"""

import cPickle

from os.path import join
from simulations import simulation_steps
from configuration import constants

outfolder = constants.output_folder_prefix

def run_multiples(run_number, years):

    start_run = run_number[0]
    end_run = run_number[1]
    for r in range(start_run, end_run):

        print 'Run {0} started'.format(r)
        m, c = simulation_steps(years)

        with open(join(outfolder, 'mothers_stats_run_{0}.pkl'.format(r)), 'wb') as f:
            cPickle.dump(m, f)
        with open(join(outfolder, 'mothers_stats_run_{0}.pkl'.format(r)), 'wb') as f:
            cPickle.dump(c, f)

        print 'Run {0} finished'.format(r)

        break

    return


if __name__ == '__main__':

    start_run = 0
    end_run = 1
    years = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    run_multiples([start_run, end_run], years)