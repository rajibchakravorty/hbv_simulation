

from population_groups import HEALTHY, CURED, INFECTED, SUSCEPTIBLE
from transitions import HealthTransformation


transition_healthy = HealthTransformation(name=HEALTHY,
                                          transformation_probabilities={
                                              HEALTHY: 1.0, CURED: 0.0,
                                              INFECTED: 0.0, SUSCEPTIBLE: 0.0})

transition_cured = HealthTransformation(name=CURED,
                                        transformation_probabilities={
                                            HEALTHY: 0.0, CURED: 1.0,
                                            INFECTED: 0.0, SUSCEPTIBLE: 0.0})

male_transition_susceptible = HealthTransformation(name=SUSCEPTIBLE,
                                                   transformation_probabilities={
                                                       HEALTHY: 0.0, CURED: 0.0,
                                                       INFECTED: 0.2, SUSCEPTIBLE: 0.8})

male_transition_infected = HealthTransformation(name=INFECTED,
                                                transformation_probabilities={
                                                    HEALTHY: 0.0, CURED: 0.8,
                                                    INFECTED: 0.2, SUSCEPTIBLE: 0.0})

male_transition_matrix = {HEALTHY: transition_healthy,
                          SUSCEPTIBLE: male_transition_susceptible,
                          INFECTED: male_transition_infected,
                          CURED: transition_cured}


female_transition_matrix = male_transition_matrix

newborn_transition_susceptible = HealthTransformation(name=SUSCEPTIBLE,
                                                      transformation_probabilities={
                                                       HEALTHY: 0.0, CURED: 0.0,
                                                       INFECTED: 0.4, SUSCEPTIBLE: 0.6})

newborn_transition_infected = HealthTransformation(name=INFECTED,
                                                   transformation_probabilities={
                                                       HEALTHY: 0.0, CURED: 0.2,
                                                       INFECTED: 0.8, SUSCEPTIBLE: 0.0})

newborn_transition_matrix = {HEALTHY: transition_healthy,
                             SUSCEPTIBLE: newborn_transition_susceptible,
                             INFECTED: newborn_transition_infected,
                             CURED: transition_cured}

infant_transition_susceptible = HealthTransformation(name=SUSCEPTIBLE,
                                                     transformation_probabilities={
                                                         HEALTHY: 0.0, CURED: 0.0,
                                                         INFECTED: 0.8, SUSCEPTIBLE: 0.2})

infant_transition_infected = HealthTransformation(name=INFECTED,
                                                  transformation_probabilities={
                                                      HEALTHY: 0.0, CURED: 0.3,
                                                      INFECTED: 0.7, SUSCEPTIBLE: 0.0})

infant_transition_matrix = {HEALTHY: transition_healthy,
                            SUSCEPTIBLE: infant_transition_susceptible,
                            INFECTED: infant_transition_infected,
                            CURED: transition_cured}

child_transition_susceptible = HealthTransformation(name=SUSCEPTIBLE,
                                                    transformation_probabilities={
                                                        HEALTHY: 0.0, CURED: 0.0,
                                                        INFECTED: 0.5, SUSCEPTIBLE: 0.5})

child_transition_infected = HealthTransformation(name=INFECTED,
                                                 transformation_probabilities={
                                                     HEALTHY: 0.0, CURED: 0.4,
                                                     INFECTED: 0.6, SUSCEPTIBLE: 0.0})

child_transition_matrix = {HEALTHY: transition_healthy,
                           SUSCEPTIBLE: child_transition_susceptible,
                           INFECTED: child_transition_infected,
                           CURED: transition_cured}

child_adult_transition_matrix = child_transition_matrix

if __name__ == '__main__':
    pass


