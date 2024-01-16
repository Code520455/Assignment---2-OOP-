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
    