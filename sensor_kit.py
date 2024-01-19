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
    def price(self) -> float:
        '''Get the total price of the circuit kit.'''
        total = 0.0
        total += self._power_supply[0].price * self._power_supply[1]
        total += self._sensor.price
        total += self._output_component.price
        total += self._wire[0].price * self._wire[1]
        if self._switch is not None:
            total += self._switch.price
        return total    
    
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
    
    
    @property
    def wire(self) -> Tuple[Wire, int]:
        '''Get the wire in the sensor circuit kit.'''
        return self._wire

    def check_complete_and_functional(self) -> bool:
        '''Check if the sensor circuit kit is complete and functional.'''
        if self._power_supply is None or self._sensor is None or self._output_component is None or self._wire is None:
            return False
        return True

    def __hash__(self):
        '''
        Hash function

        Returns:
        - Hashing of name
        '''
        return hash(self.name)

    def display_details(self) -> str:
        '''Display the details of the sensor circuit kit.'''
        data = f"{self.count} PIECE SENSOR CIRCUIT WITH "
        data += f"{self.power_supply[1]} X {self.power_supply[0].display_user_friendly()} "
        data += f"1 X {self.sensor.display_user_friendly()} "
        data += f"1 X {self._output_component.display_user_friendly()}"
        if self._switch is not None:
            data += f" 1 X {self._switch.display_user_friendly()}"
        return data

    def display_csv(self) -> str:
        '''Display the details of the sensor circuit kit.'''
        # syntaxx
        # 2,Sensor Circuit,1,Solar Panel,1.8,0.6,16.00,1,Buzzer,240,90,4,120,5.6,1,Sensor,motion,5,3.9,4,Wire,40,2.4,1,Switch,toggle,4.5,4.8
        # first circuit info
        data = f"{self.count},Sensor Circuit,"
        # power supply info
        data += f"{self.power_supply[1]},{self.power_supply[0].display_csv()},"
        # output info
        data += f"1,{self._output_component.display_csv()},"
        # sensor info
        data += f"1,{self.sensor.display_csv()},"
        # wire info
        data += f"{self._wire[1]},{self._wire[0].display_csv()}"
        # switch info
        if self._switch is not None:
            data += f",1,{self._switch.display_csv()}"
        return data
