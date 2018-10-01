"""
Iterates for a number of years and collects the health status of
each individual
"""

from adult import initialize_mothers, is_mother_giving_birth, \
    is_mother_dead_at_birth, is_adult_dead
from children import create_child, is_child_dead

import constants

from states import HEALTHY, INFECTED, SUSCEPTIBLE, CURED, DEAD, \
    INFANT_DEATH, CHILD_DEATH, MATERNAL_DEATH, HBV_DEATH

from person import ADULT, INFANT, CHILD

import stats

import cPickle


def simulation_steps(years):

    # initialize all mothers first;
    mothers = initialize_mothers(constants.INITIAL_MOTHERS)
    # mothers are all created in year = 0
    # first children are born in year =1
    year = years[1]
    # holder for all children
    children = []
    for m in mothers:

        # see if the adult naturally dies
        maternal_death = is_adult_dead()
        if maternal_death:
            m.kill(year, DEAD)
            continue

        # see if mother's health needs to change
        m.get_next_health_status()
        # update the mother's health history
        m.update_history(year, m.health_status)

        # can the mother give birth in this year
        is_giving_birth = is_mother_giving_birth()

        # if not, continue with the next mother
        if not is_giving_birth:
            continue

        # finally create the child
        child = create_child(HEALTHY, m, year)

        children.append(child)

        # see if the mother dies at child birth
        maternal_death = is_mother_dead_at_birth()

        # if she does, record it
        if maternal_death:
            m.kill(year, MATERNAL_DEATH)

    for year in years[2:]:

        for m in mothers:

            # check if this mother is alive
            if not m.is_alive:
                continue

            # check if the mother dies naturally
            maternal_death = is_adult_dead()
            if maternal_death:
                m.kill(year, DEAD)
                continue

            # change mother's health status
            m.get_next_health_status()
            m.update_history(year, m.health_status)

            # can she give birth?
            is_giving_birth = is_mother_giving_birth()

            if is_giving_birth:

                # add a new child
                child = create_child(HEALTHY, m, year)
                children.append(child)

            # is she alive after child birth?
            maternal_death = is_mother_dead_at_birth()

            if maternal_death:
                m.kill(year, MATERNAL_DEATH)

        # loop for all the children now
        for c in children:

            # if the child is not alive, continue with the next child
            if not c.is_alive:
                continue

            # if the child is born this year, continue
            if c.birth_year == year:
                continue

            # check if the child is still infant/child/adult
            c.become_child_or_adult(year)

            # change the child health status if required
            child_health_status = c.get_health_status(year-1)

            if child_health_status is None:
                continue

            # add probability over natural probability, if the child
            # is infected
            add_prob = 0.
            if child_health_status == INFECTED:
                if child.person_type == INFANT:
                    add_prob = constants.ADD_INFANT_DEATH_PROB
                elif child.person_type == CHILD:
                    add_prob = constants.ADD_CHILD_DEATH_PROB

            # determine if the child is dead
            child_death = is_child_dead(add_prob)
            if child_death:
                if add_prob > 0.:
                    c.kill(year, HBV_DEATH)
                elif c.person_type == INFANT:
                    c.kill(year, INFANT_DEATH)
                elif c.person_type == CHILD:
                    c.kill(year, CHILD_DEATH)
                else:
                    c.kill(year)
                continue

            # if not dead, see if the health status needs to change
            # and update history
            c.get_next_health_status()
            c.update_history(year, c.health_status)

    return mothers, children


if __name__ == '__main__':

    years = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mothers, children = simulation_steps(years)

    # collect the information, serialize it and save it
    mother_status = [HEALTHY, SUSCEPTIBLE, INFECTED, CURED, DEAD, MATERNAL_DEATH]
    mother_stats = stats.yearly_collection_stats(mothers, years, mother_status)
    child_status = [HEALTHY, SUSCEPTIBLE, INFECTED, CURED, DEAD, INFANT_DEATH, CHILD_DEATH, HBV_DEATH]
    children_stats = stats.yearly_collection_stats(children, years, child_status)

    print 'Mother'
    for st in mother_status:
        print '{0} : {1}'.format(st, mother_stats[st])
    print 'Children'
    for st in child_status:
        print '{0}: {1}'.format(st, children_stats[st])

    with open('mother_stats.pkl', 'wb') as f:
        cPickle.dump(mother_stats, f)

    with open('children_stats.pkl', 'wb') as f:
        cPickle.dump(children_stats, f)






