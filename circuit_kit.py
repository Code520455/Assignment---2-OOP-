# File: light_kit.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: light_kit class
# This is my own work as defined by the Academic Integrity Policy

from typing import Dict
from component import Component
from solar_panel import SolarPanel
from battery import Battery

class CircuitKit:
    def __init__(self, name: str, count: int) :
        self._name = name
        self._count = count

    @property
    def name(self) -> str:
        '''Get the name of the circuit kit.'''
        return self._name
    
    @property
    def count(self) -> int:
        '''Get the quantity of the circuit kit.'''
        return self._count
    
    @count.setter
    def count(self, count: int) -> None:
        '''Set the quantity of the circuit kit'''
        self._count = count

    @property
    def count(self) -> int:
        '''Get the quantity of the circuit kit'''
        return self._count
    
    @count.setter
    def count(self, count:int) -> None:
        '''Set the quantity of the circuit kit'''
        self._count = count

    @property
    def components(self) -> Dict[Component, int]:
        '''Get the dict of components in the circuit kit.'''
        pass

    @property
    def price(self) -> float:
        pass
    
    @property
    def component_count(self) -> int:
        '''Get the total number of components in the circuit kit'''
        return sum(self._components.values())
    
    def add_component(self, component: Component, quantity: int) -> None:
        '''Add a component to the circuit kit.'''
        self._components[component] = quantity

    def remove_component(self, component: Component) -> None:
        '''Remove a component from the circuit kit.'''
        if component in self._components:
            self._components.pop(component)

    
    def identify_power_source(self) -> bool:
        '''Check if only one type of power supply is used in the circuit kit.'''

