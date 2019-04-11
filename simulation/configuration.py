"""
Various constants for the simulation
"""

import numpy as np

from population_groups import (HEALTHY, INFECTED, SUSCEPTIBLE, CURED,
                               MALE_GENDER, FEMALE_GENDER)

# distribution of mother population at the start of the simulation

INITIAL_MOTHERS = {HEALTHY: 650000,
                   INFECTED: 25000,
                   CURED: 25000,
                   SUSCEPTIBLE: 300000}

# ADULT HBV prevelance and exposure rate
ADULT_HBV_PREVALENCE = 0.05
ADULT_EXPOSURE_RATE = 0.40

# exposure rate for child and infants
# infants are 0-1 year
# children are 1-5 years
# after 5 years healthy/cured children follow adult
# parameters; only the infected children do not have
# the same cure rate as adults
INFANT_EXPOSURE_RATE = 0.157
CHILD_EXPOSURE_RATE = 0.179

## Mother related params
MATERNAL_MORTALITY_RATE = 176 / 100000.
NATURAL_BIRTH_RATE = 20./1000. #2.14
BIRTH_PROB = (NATURAL_BIRTH_RATE/35.) * np.exp(-NATURAL_BIRTH_RATE/35.)
ADULT_MORTALITY_RATE = {HEALTHY: 5.40 / 1000.,
                        SUSCEPTIBLE: 5.40 / 1000.,
                        INFECTED: 5.40 / 1000., CURED: 5.40 / 1000.}

##INFANT/Child PARAMETER
#NEONATAL_MORTALITY_RATE = 23.3 / 1000.  # @birth
#INFANT_MORTALITY_RATE = 30.7 / 1000.  #< 1 year
#CHILD_MORTALITY_RATE = 37.6 / 1000.  # < 5 years

#vaccination
NEWBORN_VACCINATION_RATE = {MALE_GENDER: 0.80, FEMALE_GENDER: 0.80}
MAX_VACCINATION_YEAR = 2

#add to the natural mortality rate due to infection
ADD_NEONATAL_DEATH_PROB = 0.4
ADD_INFANT_DEATH_PROB = 0.3
ADD_CHILD_DEATH_PROB = 0.2

MALE_MORTALITY_RATE = {HEALTHY: 0.02, SUSCEPTIBLE: 0.02, INFECTED: 0.03, CURED: 0.02}
FEMALE_MORTALITY_RATE = {HEALTHY: 0.02, SUSCEPTIBLE: 0.02, INFECTED: 0.03, CURED: 0.20}
NEONATAL_MORTALITY_RATE = {HEALTHY: 23.3 / 1000., SUSCEPTIBLE: 25.3 / 1000., INFECTED: 27.3 / 1000., CURED: 23.3 / 1000.}
INFANT_MORTALITY_RATE = {HEALTHY: 30.7 / 1000., SUSCEPTIBLE: 35.7 / 1000., INFECTED: 40.7 / 1000., CURED: 30.7 / 1000.}
CHILD_MORTALITY_RATE = {HEALTHY: 37.6 / 1000., SUSCEPTIBLE: 40.6 / 1000., INFECTED: 45.6 / 1000., CURED: 37.6 / 1000.}




output_folder_prefix = 'config_1'