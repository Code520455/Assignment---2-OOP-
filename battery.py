# File: battery.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: component class
# This is my own work as defined by the Academic Integrity Policy

#---Rahul Saha---
from power_supply import PowerSupply

class Battery(PowerSupply):
    '''
    Represents a battery component used as a power source.

    Attributes:
    - name (str): The name of the battery.
    - size (str): The size of the battery (e.g., AA, AAA).
    - voltage (float): The voltage of the battery in volts.
    - price (float): The price of the battery in dollars and cents.

    '''

    def __init__(self, name: str, size: str, voltage: float, price: float):
        super().__init__(name, price, voltage)
        self._size = size
        self._voltage = voltage

    @property
    def size(self) -> str:
        '''Get the size of the battery'''
        return self._size
    
    def duplicate(self)