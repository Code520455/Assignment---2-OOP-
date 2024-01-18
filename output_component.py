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
        self._voltage = value

    @property
    def current(self) -> float:
        '''Get the current of the output component'''
        return self._current
    
    @current.setter
    def current(self, value: float) -> None:
        '''Set the current of the output component'''
        self._current = value

    @abstractmethod
    def parse_csv(self, csv_string: str) -> 'OutputComponent':
        '''
        Parse a CSV string to recreate an output component object.

        Parameters:
        - csv_string (str): The CSV string containing output component information.

        Returns:
        - OutputComponent: A new output component object.
        '''
        pass

    @abstractmethod
    def __eq__(self, __value: object) -> bool:
        '''
        Compare if two output component objects are equal.

        Parameters:
        - other (OutputComponent): The other output component to compare.

        Returns:
        - bool: True if the output components are equal, False otherwise.
        '''
        pass
    
    @abstractmethod
    def display_user_friendly(self) -> str:
        '''Display the output component in a user-friendly format.'''
        pass

    @abstractmethod
    def display_csv(self) -> str:
        '''Display the output component as a CSV string.'''
        pass

    def calculate_watt(self) -> float:
        '''Calculate the wattage of the output component.'''
        return self.voltage * self.current
    