#/usr/bin/env python

# Calculate the weekly dose rate for a user

# For millirem/week use constant
# 0.529 mrem-m^2 / mCi-h

# For MBq/week use constant
# 0.143 microSv-m^2 / MBq-h


def dose_rate(avg_activity,
              fraction_of_week,
              distance,
              constant=0.529):
    return constant * avg_activity \
        * fraction_of_week / distance ** 2
