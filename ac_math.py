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
    def get_inductive_reactance(f,l):
        xl = 2*3.14*f*l
        return xl
        

    @staticmethod
    def get_circuit_current(z,vs):
        i = z/.vs
        return i

    @staticmethod
    def get_supply_frequency(l,xl,):
        f = xl/(2*3.14*l)
        return f

    @staticmethod
    def get_circuit_resistance(vs,i):
        r = vs*i
        return r

    @staticmethod
    def get_circuit_resistance_2(xl,r):
        z= math.sqrt(xl**2+r**2))
        return z


# these are TODO
class RC_CIRCUIT():
    pass


class RLC_CIRCUIT():
    pass
