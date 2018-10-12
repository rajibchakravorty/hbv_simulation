"""
Various constants for the simulation
"""

import numpy as np

# 4 HBV related health states
SUSCEPTIBLE = 'susceptible'
CURED = 'cured'
HEALTHY = 'healthy'
INFECTED = 'infected'

# 4 types of death events
DEAD = 'dead'
INFANT_DEATH = 'neonatal death'
CHILD_DEATH = 'child death'
MATERNAL_DEATH = 'maternal death'
HBV_DEATH = 'hbv death'


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
NATURAL_BIRTH_RATE = 2.14
BIRTH_PROB = np.exp(-NATURAL_BIRTH_RATE)
ADULT_MORTALITY_RATE = 5.40 / 1000

##INFANT/Child PARAMETER
NEONATAL_MORTALITY_RATE = 23.3 / 1000.  # @birth
INFANT_MORTALITY_RATE = 30.7 / 1000.  #< 1 year
CHILD_MORTALITY_RATE = 37.6 / 1000.  # < 5 years

#vaccination
VACCINATION_RATE = 1.00

#add to the natural mortality rate due to infection
ADD_NEONATAL_DEATH_PROB = 0.4
ADD_INFANT_DEATH_PROB = 0.3
ADD_CHILD_DEATH_PROB = 0.2

output_folder_prefix = 'config_1'



