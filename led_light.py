# File: led_light.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: led_light class
# This is my own work as defined by the Academic Integrity Policy

from light_globe import Light
class LEDLight(Light):
    '''
    Class representing an LED light. This class is a subclass of Light.

    Additional Attributes:
    - light_type (str): The type of the LED light (e.g., white, red, green, blue, yellow, orange, pink, aqua, violet).

    Author: Rajeswari Roy
    '''

    def __init__(self, name:str, price:float, voltage:float, current_mA: float, color: str):
        super().__init__(name, price, voltage, current_mA, color)

    def duplicate(self) -> 'LEDLight':
        '''Create a duplicate copy of the LED Light'''
        return LEDLight(self.name, self.price, self.voltage, self.current, self.color)
    
    def parse_csv(self, csv_string:str) -> 'LEDLight':
        '''
        Parse a CSV string to recreate an LED light object.

        Parameters:
        - csv_string (str): The CSV string containing LED light information.

        Returns:
        - LEDLight: A new LED light object.
        '''
        name, price, voltage, current, color, light_type = csv_string.split(',')
        return LEDLight(name, float(price), float(voltage), float(current), color)      