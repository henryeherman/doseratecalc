#/usr/bin/env python

# Calculate the average activity of exposure
# As time goes up, the average exposure falls as expected
import numpy as np


def average_activity(starting_activity, half_life, to, tf):
    """ Calculate the average activity a user is exposed to,
    given a starting activity, the half life of the isotope and the
    starting and final times
    """
    to = float(to)
    tf = float(tf)
    half_life = float(half_life)
    num0 = np.exp(-1.0 * to * np.log(2.0) / half_life)
    num1 = (1.0 - np.exp(-1.0 * (np.log(2.0) * (tf - to)) / half_life))
    denom = (np.log(2.0) * (tf - to) / half_life)
    avg_act = starting_activity * num0 * num1 / denom
    return avg_act
