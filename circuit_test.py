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

        self.assertEqual(3, light_kit.count)
        self.assertEqual(light_info, light_kit.light)
        self.assertEqual(switch_info, light_kit.switch)
        self.assertEqual(2, light_kit.display_number_of_switch())
        self.assertEqual(2, light_kit.display_unique_colors())
        self.assertTrue(light_kit.check_complete_and_functional())
        self.assertEqual(25.4, light_kit.price)
        self.assertEqual(2, light_kit.display_number_of_switch())

        expected = '3 PIECE LIGHT CIRCUIT WITH 4 X 1.5V AA BATTERY $3.10 3 X 2.2V 3.2mA warm Light Globe $2.00 2 X 1.0V push Switch $1.00'
        self.assertEqual(expected, light_kit.display_details())

        expected = '3,Light Circuit,4,Battery,AA,1.5,3.10,3,Light Globe,warm,2.2,3.2,2.00,5,Wire,1.0,1.00,2,Switch,push,1.0,1.00'
        self.assertEqual(expected, light_kit.display_csv())


    def test_sensor_kit(self):
        """
        Test the sensor kit class
        """

        sensor_info = Sensor('Sensor', 5, 3.9, 'motion')
        battery_info = (Battery('Battery', 'AA', 1.5, 3.1), 4)
        buzzer = Buzzer('Buzzer', 1.0, 1.0, 240, 90, 30)
        wire_info = (Wire('Wire', 1.0, 1.0), 5)
        kit = SensorCircuitKit("Sensor Kit", 3, battery_info, sensor_info, buzzer, wire_info)


        self.assertEqual(3, kit.count)
        self.assertEqual(battery_info, kit.power_supply)
        self.assertEqual(sensor_info, kit.sensor)
        # self.assertTrue(kit.check_complete_and_functional())
        self.assertEqual(23.4, kit.price)

        expected = '3 PIECE SENSOR CIRCUIT WITH 4 X 1.5V AA Battery $3.10 1 X 3.9V motion Sensor $5.00 1 X 1.0V 240mA 90Hz 30dB Buzzer $1.00'
        self.assertEqual(expected, kit.display_details())

        expected = '3,Sensor Circuit,4,Battery,AA,1.5,3.10,1,Buzzer,90,30,1.0,240,1.00,1,Sensor,motion,3.9,5.00,5,Wire,1.0,1.00'
        self.assertEqual(expected, kit.display_csv())

        # now kit with switch
        switch = Switch('Switch', 1.0, 1.0, 'push')
        kit = SensorCircuitKit('Sesnor Kit', 3, battery_info, sensor_info, buzzer, wire_info, switch)

        self.assertEqual(3, kit.count)
        self.assertEqual(battery_info, kit.power_supply)
        self.assertEqual(sensor_info, kit.sensor)
        self.assertEqual(switch, kit.switch)
        self.assertEqual(24.4, kit.price)

        expected = '3 PIECE SENSOR CIRCUIT WITH 4 X 1.5V AA Battery $3.10 1 X 3.9V motion Sensor $5.00 1 X 1.0V 240mA 90Hz 30dB Buzzer $1.00 1 X 1.0V push Switch $1.00'
        self.assertEqual(expected, kit.display_details())

        expected = '3,Sensor Circuit,4,Battery,AA,1.5,3.10,1,Buzzer,90,30,1.0,240,1.00,1,Sensor,motion,3.9,5.00,5,Wire,1.0,1.00,1,Switch,push,1.0,1.00'
        self.assertEqual(expected, kit.display_csv())

        # now kit with light globe instead of buzzer
        light_info = LightGlobe('Light Globe', 2.0, 2.2, 3.2, "warm")
        kit = SensorCircuitKit("Sensor Kit", 3, battery_info, sensor_info, light_info, wire_info, switch)

        self.assertEqual(3, kit.count)
        self.assertEqual(battery_info, kit.power_supply)
        self.assertEqual(sensor_info, kit.sensor)
        self.assertEqual(switch, kit.switch)
        self.assertEqual(25.4, kit.price)

        expected = '3 PIECE SENSOR CIRCUIT WITH 4 X 1.5V AA Battery $3.10 1 X 3.9V motion Sensor $5.00 1 X 2.2V 3.2mA warm Light Globe $2.00 1 X 1.0V push Switch $1.00'
        self.assertEqual(expected, kit.display_details())

        expected = '3,Sensor Circuit,4,Battery,AA,1.5,3.10,1,Light Globe,warm,2.2,3.2,2.00,1,Sensor,motion,3.9,5.00,5,Wire,1.0,1.00,1,Switch,push,1.0,1.00'
        self.assertEqual(expected, kit.display_csv())

        # now kit with led light
        led_light = LEDLight('LED Light', 1.0, 1.0, 1.0, 1.0)
        kit = SensorCircuitKit("Sensor Kit", 3, battery_info, sensor_info, led_light, wire_info, switch)

        expected = '3 PIECE SENSOR CIRCUIT WITH 4 X 1.5V AA Battery $3.10 1 X 3.9V motion Sensor $5.00 1 X 1.0V 1.0mA 1.0 LED Light $1.00 1 X 1.0V push Switch $1.00'
        self.assertEqual(expected, kit.display_details())

        expected = '3,Sensor Circuit,4,Battery,AA,1.5,3.10,1,LED Light,1.0,1.0,1.0,1.00,1,Sensor,motion,3.9,5.00,5,Wire,1.0,1.00,1,Switch,push,1.0,1.00'
        self.assertEqual(expected, kit.display_csv())



unittest.main()
