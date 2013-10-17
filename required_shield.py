#/usr/bin/env python
import numpy as np


def calc_required_shield(target_exposure,
                         actual_exposure,
                         material_constant=5.0):
    XBarrier = target_exposure / actual_exposure
    NHVL = -1.0 * np.log(XBarrier) / np.log(2.0)
    HVL = material_constant
    barrier_thickness = HVL * NHVL
    return barrier_thickness
