import unittest
from ac_math import RL_CIRCUIT
class TestRl_circuit(unittest.TestCase):
    def test_resistor_voltage(self):
        volt = RL_CIRCUIT()
        result = volt.get_resistor_voltage(3,50)
        self.assertEqual(result,150)

    def test_supply_voltage(self):
        volt = RL_CIRCUIT()
        result = int(volt.get_supply_voltage(200,50))
        self.assertEqual(result,206)

    def test_inductor_voltage(self):
        volt = RL_CIRCUIT()
        result = volt.get_inductor_voltage(3,30)
        self.assertEqual(result,90)

    def test_pahse_angle(self):
        volt = RL_CIRCUIT()
        result = volt.get_phase_angle(float(50),29)
        self.assertEqual(result,0.5255837935516102)

    def test_inductive_reactance(self):
        volt = RL_CIRCUIT()
        result = volt.get_inductive_reactance(100,3)
        self.assertEqual(result,1884)

    def test_circuit_current(self):
        volt = RL_CIRCUIT()
        result = volt.get_circuit_current(40,float(100))
        self.assertEqual(result,0.4)

    def test_supply_frequency(self):
        volt = RL_CIRCUIT()
        result = int(volt.get_supply_frequency(3,40))
        self.assertEqual(result,2)

    def test_circuit_resistance(self):
        volt = RL_CIRCUIT()
        result = volt.get_circuit_resistance(100,2)
        self.assertEqual(result,200)

    def test_circuit_resistance_2(self):
        volt = RL_CIRCUIT()
        result = int(volt.get_circuit_resistance_2(19,26))
        self.assertEqual(result,32)

if __name__ == '__main__':
    unittest.main()
