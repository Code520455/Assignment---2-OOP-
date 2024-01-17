# File: circuit_test.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: circuit_test class
# This is my own work as defined by the Academic Integrity Policy

import unittest

from light_kit import LightCircuitKit
from sensor_kit import SensorCircuitKit
from light_globe import LightGlobe
from led_light import LEDLight
from switch import Switch
from wire import Wire
from battery import Battery
from power_supply import PowerSupply
from sensor import Sensor
from buzzer import Buzzer

class CircuitTest(unittest.TestCase):
    def test_light_kit(self):
        '''
        Test the light kit class
        '''
        light_info = (LightGlobe('Light Globe', 2.0, 2.2, 3.2, "warm"), 3)
        battery_info = (Battery('Battery',"AA", 1.5, 3.1), 4)
        switch_info = (Switch('Switch', 1.0, 1.0, 'push'), 2)
        wire_info = (Wire('Wire', 1.0, 1.0), 5)
        light_kit = LightCircuitKit("Light Kit", 3, light_info, switch_info, battery_info,wire_info)
