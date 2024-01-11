# File: light.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: component class
# This is my own work as defined by the Academic Integrity Policy

from multiprocessing import Value
from output_component import OutputComponent
from abc import ABC, abstractmethod

class Light(OutputComponent, ABC):
    '''
    Abstract class representing a light. This class is a subclass of OutputComponent.
    Attributes:
    - name (str): The name of the light
    - price (float): The price of the light in dollars and cents
    - voltage (float): The voltage of the light in volts.
    - current (float): The current of the light in milliamps.
    - color (str): The color of the light.
    Author: Rahul Saha
    '''

    def __init__(self, name: str, price:float, voltage:float, current_mA: float, color:str):
        super().__init__(name, price, voltage, current_mA)
        self._color = color

    @property
    def color(self) -> str:
        '''Get the colour of the light''' 
        self._color = Value

    @abstractmethod
    def duplicate(self) -> 'Light':
        '''Create a duplicate copy of the light'''
        pass

    @abstractmethod
    def parse_csv(self, csv_string: str) -> 'Light':
        '''
        Parse a CSV string to recreate a light object.

        Parameters:
        - csv_string (str): The CSV string containing light information.

        Returns:
        - Light: A new light object.
        '''
        pass


    @abstractmethod
    def __eq__(self, other: 'Light') -> bool:
        '''
        Compare if two light components are equal.

        Parameters:
        - other (Light): The other light to compare.

        Returns:
        - bool: True if the lights are equal, False otherwise.
        '''
        pass


    @abstractmethod
    def display_user_friendly(self) -> str:
        '''Display the light in a user-friendly format.'''
        pass

    @abstractmethod
    def display_csv(self) -> str:
        '''Display the light as a CSV string.'''
        pass