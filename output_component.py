# File: output_component.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: output_component class
# This is my own work as defined by the Academic Integrity Policy

from component import Component
from abc import ABC, abstractmethod

class OutputComponent(Component, ABC):
    '''
    Abstract class representing an output component. This class is a subclass of Component.

    Attributes:
    - name (str): The name of the output component.
    - price (float): The price of the output component in dollars and cents.
    - voltage (float): The voltage of the output component in volts.
    - current (float): The current of the output component in amperes.

    Author: Rahul Saha
    '''

    def __init__(self, name: str, price: float, voltage: float, current: float):
        super().__init__(name, price)
        self._voltage = voltage
        self._current = current

    @property
    def voltage(self) -> float:
        '''Get the voltage of the output component'''
        return self._voltage
    
    @voltage.setter
    def voltage(self, value: float) -> None:
        '''Set the voltage of the output component'''