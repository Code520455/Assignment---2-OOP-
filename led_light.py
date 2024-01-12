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
    
    def __eq__(self, other: 'LEDLight') -> bool:
        '''
        Compare if two LED light components are equal.

        Parameters:
        - other (LEDLight): The other LED light to compare.

        Returns:
        - bool: True if the LED lights are equal, False otherwise.
        '''
        return isinstance(other, LEDLight) and \
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
        '''Display the LED light in a user-friendly format.'''
        return f"{self.voltage}V {self.current}mA {self.color} {self.name} ${self.price:.2f}"

    def display_csv(self) -> str:
        '''Display the LED light as a CSV string.'''
        return f"{self.name},{self.color},{self.voltage},{self.current},{self.price:.2f}"
