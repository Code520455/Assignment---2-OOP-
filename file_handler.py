# File: file_handler.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: It will handle the other classes
# This is my own work as defined by the Academic Integrity Policy

from typing import Dict
from component import Component
from wire import Wire
from battery import Battery
from solar_panel import SolarPanel
from light_globe import LightGlobe
from led_light import LEDLight
from switch import Switch
from sensor import Sensor
from buzzer import Buzzer

FILE_NAME = "circuits.csv"

def load_data() -> Dict[Component, int]:
    '''
    Load data from the circuits.csv file and return a dictionary of components with quantities.

    Returns:
    - Dict[Component, int]: A dictionary where keys are Component objects and values are their quantities.
    '''
