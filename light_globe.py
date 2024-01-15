# File: light_globe.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: light_globe class
# This is my own work as defined by the Academic Integrity Policy

from light import Light


class LightGlobe(Light):
    '''
    Class representing a light globe. This class is a subclass of Light.

    Additional Attributes:
    - light_type (str): The type of the light globe (e.g., warm white, cool white, neutral white).

    Author: Rajeswari Roy
    '''
    light_globe_colors = ["warm", "cool", "neutral"]

    def __init__(self, name: str, price: float, voltage: float, current_mA: float, color: str):
        super().__init__(name, price, voltage, current_mA, color)

    def duplicate(self) -> 'LightGlobe':
        '''Create a duplicate copy of the light globe.'''
        return LightGlobe(self.name, self.price, self.voltage, self.current, self.color)

    def parse_csv(self, csv_string: str) -> 'LightGlobe':
        '''
        Parse a CSV string to recreate a light globe object.

        Parameters:
        - csv_string (str): The CSV string containing light globe information.

        Returns:
        - LightGlobe: A new light globe object.
        '''
        name, price, voltage, current, color = csv_string.split(',')
        return LightGlobe(name, float(price), float(voltage), float(current), color)
