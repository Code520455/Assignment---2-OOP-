# File: power_supply.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: power supply class
# This is my own work as defined by the Academic Integrity Policy

from component import Component
from abc import ABC, abstractmethod

class PowerSupply(Component, ABC):
    '''
    Abstract class representing a power supply. This class is a subclass of Component.

    Attributes:
    - name (str): The name of the power supply.
    - price (float): The price of the power supply in dollars and cents.
    - voltage (float): The voltage of the power supply in volts.

    Author: Rajeswari Roy
    '''

    def __init__(self, name: str, price: float, voltage) -> None:
        super().__init__(name, price)
        self._voltage = voltage
        
    @property
    def voltage(self) -> float:
        '''Get the voltage of the power supply'''
        return self._voltage
    
    @voltage.setter
    def voltage(self, value: float) -> None:
        '''Set the voltage of the power supply'''
        self._voltage = value

    @abstractmethod
    def duplicate(self) -> 'PowerSupply':
        '''Create a duplicate copy of the power supply'''
        pass

    @abstractmethod
    def parse_csv(self, csv_tring: str) -> 'PowerSupply':
        '''
        Parse a CSV string to recreate a power supply object.

        Parameters:
        - csv_string (str): The CSV string containing power supply information.

        Returns:
        - PowerSupply: A new power supply object.
        '''
        pass

    @abstractmethod
    def __eq__(self, other: 'PowerSupply') -> bool:
        '''
        Compare if two power supply components are equal.

        Parameters:
        - other (PowerSupply): The other power supply to compare.

        Returns:
        - bool: True if the power supplies are equal, False otherwise.
        '''
        pass

    @abstractmethod
    def display_user_friendly(self) -> str:
        '''Display the power supply in a user-friendly format.'''
        pass

    @abstractmethod
    def display_csv(self) -> str:
        '''Display the power supply as a CSV string.'''
        pass
