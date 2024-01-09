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

    def __init__(self, name:str,) -> None:
        super().__init__()