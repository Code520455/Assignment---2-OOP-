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

        wire = Wire('Wire', 1.0, 1.0)
        self.assertEqual('Wire', wire.name)
        self.assertEqual(1.0, wire.price)
        self.assertEqual(1.0, wire.length_mm)

        wire2 = wire.duplicate()
        # equality operator
        self.assertEqual(wire, wire2)

        # test the CSV parsing
        self.assertEqual(wire, wire.parse_csv('Wire,1.0,1.0'))

        # test display user friendly
        expected = '1.0mm Wire $1.00'
        self.assertEqual(expected, wire.display_user_friendly())

    def test_switch(self):
        '''
        Test the switch class
        ''' 
        switch = Switch('Switch', 1.0, 1.0, 'push')
        self.assertEqual('Switch', switch.name)
        self.assertEqual(1.0, switch.price)
        self.assertEqual(1.0, switch.voltage)

        switch2 = switch.duplicate()
        # equality operator
        self.assertEqual(switch, switch2)

        # test the CSV parsing
        self.assertEqual(switch, switch.parse_csv('Switch,1.0,1.0,push'))

        # test display user friendly
        expected = '1.0V push Switch $1.00'
        self.assertEqual(expected, switch.display_user_friendly())

    def test_solar_panel(self):
        '''
        Test the solar panel class
        '''

        solar_panel = SolarPanel('Solar Panel', 1.0,1.0,1.0)
        self.assertEqual('Solar Panel', solar_panel.name)
        self.assertEqual(1.0, solar_panel.price)
        self.assertEqual(1.0, solar_panel.voltage)
        self.assertEqual(solar_panel.current_mA)

        solar_panel2 = solar_panel.duplicate()
        # equality operator
        self.assertEqual(solar_panel, solar_panel2)

        # test the CSV parsing
        self.assertEqual(solar_panel, solar_panel.parse_csv('Solar Panel,1.0,1.0,1.0'))

        # test display user friendly
        expected = '1.0V 1.0mA Solar Panel $1.00'
        self.assertEqual(expected, solar_panel.display_user_friendly()) 

    def test_sensor(self):
        '''
        Test the sensor class
        '''
        
        sensor = Sensor('Sesnor', 1.0, 1.0, 'movement')
        self.assertEqual('Sesnor', sensor.name)
        self.assertEqual(1.0, sensor.price)
        self.assertEqual(1.0, sensor.voltage)
        self.assertEqual('movement', sensor.input_type)

        sensor2 = sensor.duplicate()
        # equality operator
        self.assertEqual(sensor, sensor2)

        # test the CSV parsing
        self.assertEqual(sensor, sensor.parse_csv('Sensor,1.0,1.0,movement'))

        # test display user friendly
        expected = '1.0V movement Sensor $1.00'
        self.assertEqual(expected, sensor.display_user_friendly())

    def test_light_globes(self):
        '''
        Test the light globe class
        '''
        light_globe = LightGlobe('Light Globe', 1.0, 1.0, 1.0, 'warm white')
        self.assertEqual('Light Globe', light_globe.name)
        self.assertEqual(1.0, light_globe.price)
        self.assertEqual(1.0, light_globe.voltage)
        self.assertEqual(1.0, light_globe.current)
        self.assertEqual('warm white', light_globe.color)
        light_globe2 = light_globe.duplicate()
        # equality operator
        self.assertEqual(light_globe, light_globe2)

        # test the CSV parsing
        self.assertEqual(light_globe, light_globe.parse_csv('Light Globe,1.0,1.0,1.0,warm white'))

        # test display user friendly
        expected = '1.0V 1.0mA warm white Light Globe $1.00'
        self.assertEqual(expected, light_globe.display_user_friendly())

