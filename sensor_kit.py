# File: app.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: This is the main application where user can do whatever they want. 
# This is my own work as defined by the Academic Integrity Policy

from circuit_kit import CircuitKit
from typing import List, Tuple, Dict
from component import Component
from power_supply import PowerSupply
from sensor import Sensor
from output_component import OutputComponent
from wire import Wire
from switch import Switch

class SensorCircuitKit(CircuitKit):
    '''
    Class representing a sensor circuit kit. This class is a subclass of CircuitKit.

    Additional Attributes:
    - power_supply (PowerSupply): The power supply in the sensor circuit kit.
    - sensor (Sensor): The sensor in the sensor circuit kit.
    - lights (List[Light]): List of lights in the sensor circuit kit.
    - switches (List[Switch]): List of switches in the sensor circuit kit.

    Author: Rahul Saha
    '''

    def __init__(self, name: str, count: int, power_supply: Tuple[PowerSupply, int], sensor: Sensor,
                 output_component: OutputComponent, wire: Tuple[Wire, int], switch: Switch=None):
        super().__init__(name, count)
        self._power_supply = power_supply
        self._sensor = sensor
        self._output_component = output_component  # either light or buzzer
        self._switch = switch
        self._wire = wire

    @property
    def components(self) -> Dict[Component, int]:
        '''Get the dict of components in the circuit kit'''
        return {self._power_supply[0]: self._power_supply[1], self._sensor: 1, self._output_component: 1, self._wire[0]: self._wire[1], self._switch: 1}

    @property
    def power_supply(self) -> Tuple[PowerSupply, int]:
        '''Get the power supply in the sensor circuit kit'''
        return self._sensor
    
    @property
    def sensor(self) -> Sensor:
        '''Get the sensor in the sensor circuit kit'''
        return self._sensor
    
    @property
    def switch(self) -> Switch:
        '''Get the list of switches in the sensor circuit kit'''
        return self._switch
    
    @property
    def output_component(self) -> OutputComponent:
        return self._output_component
