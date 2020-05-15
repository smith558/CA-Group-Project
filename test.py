import unittest
from ac_math import RL_CIRCUIT
from ac_math import RC_CIRCUIT
from ac_math import RLC_CIRCUIT

class TestRl_circuit(unittest.TestCase):
    def test_resistor_voltage(self):
        volt = RL_CIRCUIT()
        result = volt.get_resistor_voltage(3, 50)
        self.assertEqual(result, 150)

    def test_supply_voltage(self):
        volt = RL_CIRCUIT()
        result = int(volt.get_supply_voltage(200, 50))
        self.assertEqual(result, 206)

    def test_inductor_voltage(self):
        volt = RL_CIRCUIT()
        result = volt.get_inductor_voltage(3, 30)
        self.assertEqual(result, 90)

    def test_pahse_angle(self):
        volt = RL_CIRCUIT()
        result = round(volt.get_phase_angle(float(50), 29),15)
        self.assertEqual(result, 0.52558379355161)

    def test_inductive_reactance(self):
        volt = RL_CIRCUIT()
        result = volt.get_inductive_reactance(100, 3)
        self.assertEqual(result, 1884.9555921538758)

    def test_circuit_current(self):
        volt = RL_CIRCUIT()
        result = volt.get_circuit_current(40, float(100))
        self.assertEqual(result, 2.5)

    def test_supply_frequency(self):
        volt = RL_CIRCUIT()
        result = int(volt.get_supply_frequency(3, 40))
        self.assertEqual(result, 2)

    def test_circuit_resistance(self):
        volt = RL_CIRCUIT()
        result = volt.get_circuit_resistance(100, 2)
        self.assertEqual(result, 99.9799979995999)

    def test_circuit_impedence(self):
        volt = RL_CIRCUIT()
        result = int(volt.get_circuit_impedence(19, 26))
        self.assertEqual(result, 32)

class TestRC_circuit(unittest.TestCase):
    def test_resistor_voltage(self):
        volt = RC_CIRCUIT()
        result = volt.get_resistor_voltage(float(1.2), 48)
        self.assertEqual(result, 57.599999999999994)

    def test_supply_voltage(self):
        volt = RC_CIRCUIT()
        result = int(volt.get_supply_voltage(200, 50))
        self.assertEqual(result, 206)

    def test_capacitive_voltage(self):
        volt = RC_CIRCUIT()
        result = volt.get_capacitive_voltage(3, 30)
        self.assertEqual(result, 90)

    def test_pahse_angle(self):
        volt = RC_CIRCUIT()
        result = round(volt.get_phase_angle(float(10), 15), 1)
        self.assertEqual(result, 0.52558379355161)

    def test_capacitive_reactance(self):
        volt = RC_CIRCUIT()
        result = volt.get_capacitive_reactance(100, float(0.001))
        self.assertEqual(result, 1.5915494309189535)

    def test_circuit_current(self):
        volt = RC_CIRCUIT()
        result = volt.get_circuit_current(40, float(100))
        self.assertEqual(result, 2.5)

    def test_supply_frequency(self):
        volt = RC_CIRCUIT()
        result = int(volt.get_supply_frequency(float(0.001), 40))
        self.assertEqual(result, 3)

    def test_circuit_resistance(self):
        volt = RC_CIRCUIT()
        result = volt.get_circuit_resistance(100, 2)
        self.assertEqual(result, 100.0)

    def test_circuit_impedence(self):
        volt = RC_CIRCUIT()
        result = int(volt.get_circuit_impedence(19, 26))
        self.assertEqual(result, 26)

class TestRLC_circuit(unittest.TestCase):
    def test_resistor_voltage(self):
        volt = RLC_CIRCUIT()
        result = volt.get_resistor_voltage(3, 50)
        self.assertEqual(result, 150)

    def test_supply_voltage(self):
        volt = RLC_CIRCUIT()
        result = int(volt.get_supply_voltage(200, 50, 68))
        self.assertEqual(result, 200)

    def test_inductor_voltage(self):
        volt = RLC_CIRCUIT()
        result = volt.get_inductor_voltage(3, 30)
        self.assertEqual(result, 90)

    def test_pahse_angle(self):
        volt = RLC_CIRCUIT()
        result = round(volt.get_phase_angle(float(50), 29, 40))
        self.assertEqual(result, 1.0)

    def test_inductive_reactance(self):
        volt = RLC_CIRCUIT()
        result = volt.get_inductive_reactance(100, 3)
        self.assertEqual(result, 1884.9555921538758)

    def test_circuit_current(self):
        volt = RLC_CIRCUIT()
        result = volt.get_circuit_current(40, float(100))
        self.assertEqual(result, 2.5)

    def test_supply_frequency_2(self):
        volt = RLC_CIRCUIT()
        result = int(volt.get_supply_frequency_2(3, 40))
        self.assertEqual(result, 2)

    def test_circuit_resistance(self):
        volt = RLC_CIRCUIT()
        result = volt.get_circuit_resistance(float(100), 22, 40)
        self.assertEqual(result, 91.6515138991168)

    def test_circuit_impedence(self):
        volt = RLC_CIRCUIT()
        result = int(volt.get_circuit_impedence(float(19), 26, 29))
        self.assertEqual(result, 38)

    def test_capacitive_reactance(self):
        volt = RLC_CIRCUIT()
        result = volt.get_capacitive_reactance(100, float(0.001))
        self.assertEqual(result, 1.5915494309189535)

    def test_capacitive_voltage(self):
        volt = RLC_CIRCUIT()
        result = volt.get_capacitive_voltage(3, 30)
        self.assertEqual(result, 90)

    def test_supply_frequency(self):
        volt = RLC_CIRCUIT()
        result = int(volt.get_supply_frequency(float(0.1), float(40)))
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
