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
    
