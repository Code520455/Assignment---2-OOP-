# File: switch.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: switch class
# This is my own work as defined by the Academic Integrity Policy

from input_component import InputComponent

class Switch(InputComponent):
    '''
    Class representing a switch. This class is a subclass of InputComponent.

    Attributes:
    - name (str): The name of the switch.
    - price (float): The price of the switch in dollars and cents.
    - voltage (float): The voltage of the switch in volts.
    - switch_type (str): The type of the switch (e.g., push, slide, rocker, toggle).

    Author: Rajeswari Roy
    '''

    switch_types = ["push", "slide", "rocker", "toggle"]

    def __init__(self, name: str, price: float, voltage: float, switch_type: str):
        super().__init__(name, price, switch_type, voltage)

    def duplicate(self) -> 'Switch':
        '''Create a duplicate copy of the switch.'''
        return Switch(self.name, self.price, self.voltage, self.input_type)

    def parse_csv(self, csv_string: str) -> 'Switch':
        '''
        Parse a CSV string to recreate a switch object.

        Parameters:
        - csv_string (str): The CSV string containing switch information.

        Returns:
        - Switch: A new switch object.
        '''
        name, price, voltage, switch_type = csv_string.split(',')
        return Switch(name, float(price), float(voltage), switch_type)

    def __eq__(self, other: 'Switch') -> bool:
        '''
        Compare if two switch components are equal.

        Parameters:
        - other (Switch): The other switch to compare.

        Returns:
        - bool: True if the switches are equal, False otherwise.
        '''
        return isinstance(other, Switch) and \
            self.name == other.name and \
            self.price == other.price and \
            self.voltage == other.voltage and \
            self.input_type == other.input_type

    def __hash__(self):
        '''
        Hash function

        Returns:
        - Hashing of name
        '''
        return hash(self.name)

    def display_user_friendly(self) -> str:
        '''Display the switch in a user-friendly format.'''
        return f"{self.voltage}V {self.input_type} {self.name} ${self.price:.2f}"

    def display_csv(self) -> str:
        '''Display the switch as a CSV string.'''
        return f"{self.name},{self.input_type},{self.voltage},{self.price:.2f}"
 