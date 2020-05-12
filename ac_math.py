from math import sqrt, atan, acos, asin, pi
from decimal import *


class RL_CIRCUIT():

    @staticmethod
    def get_resistor_voltage(i, r):
        vr = i * r
        return vr

    @staticmethod
    def get_supply_voltage(vr, vl):
        vs = sqrt(vr ** 2 + vl ** 2)
        return vs

    @staticmethod
    def get_supply_voltage_2(i, z):
        return i * z

    @staticmethod
    def get_inductor_voltage(i, xl):
        vl = xl * i
        return vl

    @staticmethod
    def get_phase_angle(r, xl):
        o = atan(xl / r)
        return o

    @staticmethod
    def get_phase_angle_2(r, z):
        o = acos(r / z)
        return o

    @staticmethod
    def get_phase_angle_3(xl, z):
        o = asin(xl / z)
        return o

    @staticmethod
    def get_inductive_reactance(f, l):
        xl = 2 * pi * f * l
        return xl

    @staticmethod
    def get_circuit_current(z, vs):
        i = vs / z
        return i

    @staticmethod
    def get_supply_frequency(l, xl):
        f = xl / (2 * pi * l)
        return f

    @staticmethod
    def get_circuit_resistance(z, xl):
        return abs(sqrt(z ** 2 - xl ** 2))

    @staticmethod
    def get_circuit_impedence(xl, r):
        z = sqrt(xl ** 2 + r ** 2)
        return z


# these are TODO
class RC_CIRCUIT():
    
    @staticmethod
    def get_resistor_voltage(i, r):
        vr = i * r
        return vr

    @staticmethod
    def get_supply_voltage(vr, vc):
        vs = sqrt(vr ** 2 + vc ** 2)
        return vs

    @staticmethod
    def get_supply_voltage_2(i, z):
        return i * z

    @staticmethod
    def get_capacitive_voltage(i, xc):
        vc = xc * i
        return vc

    @staticmethod
    def get_phase_angle(r, xc):
        o = atan((1/xc) / r)
        return o

    @staticmethod
    def get_phase_angle_2(r, z):
        o = acos(r / z)
        return o

    @staticmethod
    def get_phase_angle_3(xc, z):
        o = asin((1/xc)/ z)
        return o

    @staticmethod
    def get_capacitive_reactance(f, c):
        xc = 1/(2 * pi * f * c)
        return xc

    @staticmethod
    def get_circuit_current(z, vs):
        i = vs / z
        return i

    @staticmethod
    def get_supply_frequency(c, xc):
        f = 1 / (2 * pi * c * xc)
        return f

    @staticmethod
    def get_circuit_resistance(z, xc):
        return abs(sqrt(z ** 2 - (1/xc) ** 2))

    @staticmethod
    def get_circuit_impedence(xc, r):
        z = sqrt((1/xc) ** 2 + r ** 2)
        return z


class RLC_CIRCUIT():
    pass
