import unittest

from wire import Wire
from switch import Switch
from solar_panel import SolarPanel
from sensor import Sensor
from light_globe import LightGlobe
from led_light import LEDLight
from buzzer import Buzzer
from battery import Battery

class ComponentTest(unittest.TestCase):
    def test_wire(self):
        '''
        Test the wire class
        '''

        