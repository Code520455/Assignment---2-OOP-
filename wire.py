# File: wire.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: wire class
# This is my own work as defined by the Academic Integrity Policy

from  import Component
from component import Component

class Wire(Component):
    '''
    Represents a wire component used to connect other components.

    Attributes:
    - name (str): The name of the wire.
    - length_mm (float): The length of the wire in millimeters.
    - price (float): The price of the wire in dollars and cents.

    Author: Rahul Saha
    '''

    def __init__(self, name: str, price: float, length_mm: float) -> None:
        super().__init__(name, price)
        self._length_mm = length_mm

    @property
    def length_mm(self) -> float:
        '''Get the length of the wire'''
        return self._length_mm
    
    @length_mm.setter
    def length_mm(self, value:float) -> None:
        '''Set the length of the wire.'''
        self._length_mm = value

    def duplicate(self) -> 'Wire':
        '''Create a duplicate copy of the wire.'''
        return Wire(self.name, self._length_mm, self.price)
    
    def parse_csv(self, csv_string: str) -> 'Wire':
        '''
        Parse a CSV string to recreate a wire object.

        Parameters:
        - csv_string (str): The CSV string containing wire information.

        Returns:
        - Wire: A new wire object.
        '''
        name, length_mm, price = csv_string.split(',')
        return Wire(name, float(length_mm), float(price))
    
    def __hash__(self):
        '''
        Hash function
        
        Returns:
        - Hashing of name
        '''
        return hash(self.name)
    
    def __eq__(self, other: 'Wire') -> bool:
        '''
        Compare if two wire components are equal.

        Parameters:
        - other (Wire): The other wire to compare.

        Returns:
        - bool: True if the wires are equal, False otherwise.
        '''