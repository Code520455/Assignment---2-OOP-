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

    def __eq__(self, other: 'LightGlobe') -> bool:
        '''
        Compare if two light globe components are equal.

        Parameters:
        - other (LightGlobe): The other light globe to compare.

        Returns:
        - bool: True if the light globes are equal, False otherwise.
        '''
        return isinstance(other, LightGlobe) and \
            self.name == other.name and \
            self.price == other.price and \
            self.voltage == other.voltage and \
            self.current == other.current and \
            self.color == other.color

    def __hash__(self):
        '''
        Hash function

        Returns:
        - Hashing of name
        '''
        return hash(self.name)

    def display_user_friendly(self) -> str:
        '''Display the light globe in a user-friendly format.'''
        return f"{self.voltage}V {self.current}mA {self.color} {self.name} ${self.price:.2f}"

    def display_csv(self) -> str:
        '''Display the light globe as a CSV string.'''
        return f"{self.name},{self.color},{self.voltage},{self.current},{self.price:.2f}"
