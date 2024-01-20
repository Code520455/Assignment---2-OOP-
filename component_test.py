# File: component_test.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: component_test
# This is my own work as defined by the Academic Integrity Policy

#This test is fully done by Rahul Saha
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

    def test_led_light(self):
        '''
        Test the LED light class
        '''

        led_light = LEDLight('LED Light', 1.0, 1.0, 1.0, 'aqua')
        self.assertEqual('LED Light', led_light.name)
        self.assertEqual(1.0, led_light.price)
        self.assertEqual(1.0, led_light.voltage)
        self.assertEqual(1.0, led_light.current)
        self.assertEqual('aqua', led_light.color)

        led_light2 = led_light.duplicate()
        # equality operator
        self.assertEqual(led_light, led_light2)

        # test the CSV parsing
        self.assertEqual(led_light, led_light.parse_csv('LED Light,1.0,1.0,1.0,aqua'))

        # test display user friendly
        expected = '1.0V 1.0mA aqua LED Light $1.00'
        self.assertEqual(expected, led_light.display_user_friendly())



    def test_buzzer(self):
        """
        Test the buzzer class
        """
        buzzer = Buzzer('Buzzer', 1.0, 1.0, 1.0, 1.0, 1.0)
        self.assertEqual('Buzzer', buzzer.name)
        self.assertEqual(1.0, buzzer.price)
        self.assertEqual(1.0, buzzer.voltage)
        self.assertEqual(1.0, buzzer.current)
        self.assertEqual(1.0, buzzer.frequency)
        self.assertEqual(1.0, buzzer.sound_pressure)

        buzzer2 = buzzer.duplicate()
        # equality operator
        self.assertEqual(buzzer, buzzer2)

        # test the CSV parsing
        self.assertEqual(buzzer, buzzer.parse_csv('Buzzer,1.0,1.0,1.0,1.0,1.0'))

        # test display user friendly
        expected = '1.0V 1.0mA 1.0Hz 1.0dB Buzzer $1.00'
        self.assertEqual(expected, buzzer.display_user_friendly())

    def test_battery(self):
        """
        Test the battery class
        """
        battery = Battery('Battery', 'AA', 1.0, 1.0)
        self.assertEqual('Battery', battery.name)
        self.assertEqual('AA', battery.size)
        self.assertEqual(1.0, battery.voltage)
        self.assertEqual(1.0, battery.price)

        battery2 = battery.duplicate()
        # equality operator
        self.assertEqual(battery, battery2)

        # test the CSV parsing
        self.assertEqual(battery, battery.parse_csv('Battery,AA,1.0,1.0'))

        # test display user friendly
        expected = '1.0V AA Battery $1.00'
        self.assertEqual(expected, battery.display_user_friendly())


unittest.main()