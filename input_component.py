# File: imput_component.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: input_component class
# This is my own work as defined by the Academic Integrity Policy

from component import Component
from abc import ABC, abstractmethod

class InputComponent(Component, ABC):
    '''
    Abstract class representing an input component. This class is a subclass of Component.

    Attributes:
    - name (str): The name of the input component.
    - price (float): The price of the input component in dollar and cents.
    - type (str): The type of the input component.
    - voltage (float): The voltage of the input component in volts.

    Author: Rajeswari Roy
    '''

    def __init__(self, name: str, price: float, input_type: str, voltage: float):
        super().__init__(name, price)
        self._input_type = input_type
        self._voltage = voltage

    @property
    def input_type(self) -> str:
        '''Get the type of the input component'''
        return self._input_type
    
    @input_type.setter
    def input_type(self, value: str) -> None:
        '''Set the type of the input component'''
        self._input_type = value
        
