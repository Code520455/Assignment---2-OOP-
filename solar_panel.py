# File: solar_panel.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: solar_panel class
# This is my own work as defined by the Academic Integrity Policy

from power_supply import PowerSupply

class SolarPanel(PowerSupply):
    '''
    Represents a solar panel power supply that works in sunlight.

    Attributes:
    - name (str): The name of the solar panel.
    - voltage (float): The voltage of the solar panel in volts.
    - current_mA (float): The current of the solar panel in milliamps.
    - price (float): The price of the solar panel in dollars and cents.

    Author: Rajeswari Roy
    '''

    def __init__(self, name: str, voltage: float, current_mA: float, price: float):
        super().__init__(name, price, voltage)
        self._current_mA = current_mA

    @property
    def current_mA(self) -> float:
        '''Get the current of the solar panel.'''
        return self._current_mA
    
    @current_mA.setter
    def current_mA(self, value:float) -> None:
        '''Set the current of the solar panel'''
        self._current_mA = value
        