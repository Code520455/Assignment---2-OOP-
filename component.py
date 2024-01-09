# File: component.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: component class
# This is my own work as defined by the Academic Integrity Policy

from abc import ABC, abstractmethod

class Component(ABC):
    '''
    Abstract base class representing a component.

    Attributes:
    - name (str): The name of the component.
    - price (float): The price of the component in dollars and cents.

    Author: Rahul Saha
    '''

    def __init__(self, name: str, price: float) -> None:
        self._name = name 
        self._price = price

    @property
    def name(self) -> str:
        '''Get the name of the component'''
        return self._name
    @name.setter
    def name(self, value:str) -> None:
        '''Set the name of the component'''
        self._name = value

    @property
    def price(self) -> float:
        '''Get the price of the component'''
        return self._price
    
    @price.setter
    def price(self, value: float) -> None:
        '''Set the price of the component'''
        self._price = value

    @abstractmethod
    def parse_csv(self, csv_tring: str):
        '''
        Parse a CSV string to recreate a component object.

        Parameters:
        - csv_string (str): The CSV string containing component information.

        Returns:
        - Component: A new component object.
        '''
        pass


    @abstractmethod
    def duplicate(self) -> 'Component':
        '''Create a duplicate copy of the component.'''
        pass

