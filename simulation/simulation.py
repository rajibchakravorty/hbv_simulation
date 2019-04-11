
from population_groups import (Person, Child, Male, Female, Couple,
                               ADULT, MALE_GENDER, FEMALE_GENDER, CHILD,
                               HEALTHY, SUSCEPTIBLE, INFECTED, CURED, DEATH,
                               INFANT_DEATH, CHILD_DEATH)


from transformations import (male_transition_matrix,
                             female_transition_matrix,
                             newborn_transition_matrix,
                             child_transition_matrix,
                             child_adult_transition_matrix)


from configuration import MALE_MORTALITY_RATE

import configuration as config
import transformations as transformations


def main():

    male = Male(birth_year=-1,
                is_married=False,
                health_status={0: HEALTHY},
                transformation_matrix=male_transition_matrix,
                death_probability=MALE_MORTALITY_RATE,
                config=None)

    children_health = dict()
    health_status = [HEALTHY, SUSCEPTIBLE, INFECTED, CURED, DEATH,
                     INFANT_DEATH, CHILD_DEATH]
    for health in health_status:
        children_health[health] = 0

    for _ in range(10000):

        female = Female(birth_year=-1,
                        is_married=True,
                        health_status={0: SUSCEPTIBLE},
                        transformation_matrix=female_transition_matrix,
                        death_probability=MALE_MORTALITY_RATE,
                        birth_probability=0.02)

        couple = Couple(female, male, config, transformations)

        for year in range(1, 13):
            couple.year_events(year)

        if couple.count_children() > 0:
            children_born.append(couple.count_children())


if __name__ == '__main__':
    main()