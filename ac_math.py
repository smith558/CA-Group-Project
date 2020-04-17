import math


class RL_CIRCUIT():

    @staticmethod
    def get_resistor_voltage(i, r):
        vr = i * r
        return vr

    @staticmethod
    def get_supply_voltage(vr, vl):
        vs = math.sqrt(vr ** 2 + vl ** 2)
        return vs

    @staticmethod
    def get_inductor_voltage(i, xl):
        vl = xl * i
        return vl

    @staticmethod
    def get_phase_angle(r, xl, xc):
        a = ((xl - xc) / r)
        o = math.atan(a)
        return o

    @staticmethod
    def get_inductive_reactance():
        pass

    @staticmethod
    def get_circuit_current():
        pass

    @staticmethod
    def get_supply_frequency():
        pass

    @staticmethod
    def get_circuit_resistance():
        pass

    @staticmethod
    def get_circuit_resistance_2():
        pass


class RC_CIRCUIT():
    pass


class RLC_CIRCUIT():
    pass
