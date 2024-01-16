# File: light_kit.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: light_kit class
# This is my own work as defined by the Academic Integrity Policy

from typing import List, Dict, Tuple
from circuit_kit import CircuitKit
from light import Light
from switch import Switch
from wire import Wire
from battery import Battery

class LightCircuitKit(CircuitKit):
    '''
    Class representing a light circuit kit. This class is a subclass of CircuitKit.

    Additional Attributes:
    - lights (List[Light]): List of lights in the light circuit kit.
    - switches (List[Switch]): List of switches in the light circuit kit.

    Author: Rahul Saha
    '''

    def __init__(self, name: str, count: int,
                 light: Tuple[Light, int], switch: Tuple[Switch, int],
                 battery: Tuple[Battery, int], wire: Tuple[Wire, int]):
        super().__init__(name, count)
        self._light: Tuple[Light, int] = light
        self._switch: Tuple[Switch, int] = switch
        self._wire = wire
        self._battery: Tuple[Battery, int] = battery

    @property
    def price(self):
        '''Get the total price of the circuit kit'''
        total = 0.0
        total += self._battery[0].price * self._battery[1]
        total += self._light[0].price * self._light[1]
        total += self._switch[0].price * self._switch[1]
        total += self._wire[0].price * self._wire[1]
        return total
    
    @property
    def component(self):
        '''Get the doct of components in the circuit kit'''
        return {self._battery[0]: self._battery[1], self._light[0]: self._light[1], self._switch[0]: self._switch[1], self._wire[0]: self._wire[1]}
