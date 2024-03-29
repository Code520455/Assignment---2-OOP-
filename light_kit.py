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

    @property
    def light(self) -> Tuple[Light, int]:
        '''Get the list of lights in the light circuit kit'''
        return self._switch
    
    @property
    def switch(self) -> Tuple[Switch, int]:
        '''Get the list of switches in the light circuit kit'''

    @property
    def battery(self) -> Tuple[Battery, int]:
        '''Get the list of switches in the light circuit kit'''
        return self._battery
    
    @property
    def wire(self) -> Tuple[Wire, int]:
        '''Get the list of switches in the light circuit kit'''
        return self._wire
    
    def display_unique_colors(self) -> int:
        '''Get the number of unique colors of lights in the light circuit kit.'''
        return 1

    def display_number_of_switch(self) -> int:
        '''Get the number of switches'''
        return self.switch[1]
    
    def display_switch_type(self) -> None:
        '''Switch type with voltage'''
        print(f"{self.switch[0].voltage}V {self.switch[0].input_type} Switch")

    def check_complete_and_functional(self) -> bool:
        '''Check if the light circuit kit is complete and functional.'''
        if self._battery is None or self.switch is None or self._light is None or self._wire is None:
            return False
        return True
    
    def __hash__(self):
        '''
        Hash function

        Returns:
        - Hashing of all variables
        '''
        hash_tuple = (self.name, self._light, self._switch, self._wire, self._battery)
        return hash(hash_tuple)

    def display_details(self) -> str:
        '''Display the details of the light circuit kit.'''
        data = f"{self.count} PIECE LIGHT CIRCUIT WITH "
        data += f"{self._battery[1]} X {self._battery[0].display_user_friendly()} "
        data += f"{self.light[1]} X {self.light[0].display_user_friendly()} "
        data += f"{self.switch[1]} X {self.switch[0].display_user_friendly()}"
        return data

    def display_csv(self) -> str:
        '''Display the details of the light circuit kit.'''
        #syntax
        # 3,Light Circuit,2,Battery,AA,1.5,3.1,4,Light Globe,warm,6.5,240,3.5,14,Wire,60,3.2,1,Switch,push,4.5,4.6
        # first circuit info
        data = f"{self.count},Light Circuit,"
        # battery info
        data += f"{self._battery[1]},{self._battery[0].display_csv()},"
        # light info
        data += f"{self.light[1]},{self.light[0].display_csv()},"
        # wire info
        data += f"{self._wire[1]},{self._wire[0].display_csv()},"
        # switch info
        data += f"{self.switch[1]},{self.switch[0].display_csv()}"
        return data
    
    