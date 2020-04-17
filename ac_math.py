import math


def get_resistor_voltage(i, r):
    vr = i * r
    return vr


def get_supply_voltage(vr, vl):
    vs = math.sqrt(vr ** 2 + vl ** 2)
    return vs


def get_inductor_voltage(i, xl):
    vl = xl * i
    return vl


def get_phase_angle(r, xl, xc):
    a = ((xl - xc) / r)
    o = math.atan(a)
    return o


def get_inductive_reactance():
    pass


def get_circuit_current():
    pass


def get_supply_frequency():
    pass


def get_circuit_resistance():
    pass


def get_circuit_resistance_2():
    pass
