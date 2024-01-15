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

    def duplicate(self) -> 'SolarPanel':
        '''Create a duplicate copy of the solar panel.'''
        return SolarPanel(self.name, self.voltage, self.current_mA, self.price)

    def parse_csv(self, csv_string: str) -> 'SolarPanel':
        '''
        Parse a CSV string to recreate a solar panel object.

        Parameters:
        - csv_string (str): The CSV string containing solar panel information.

        Returns:
        - SolarPanel: A new solar panel object.
        '''
        name, voltage, current_mA, price = csv_string.split(',')
        return SolarPanel(name, float(voltage), float(current_mA), float(price))

    def calculate_wattage(self) -> float:
        '''Calculate the wattage of the solar panel.'''
        return (self.voltage * self.current_mA) / 1000  # Convert milliamps to amps

    def __eq__(self, other: 'SolarPanel') -> bool:
        '''
        Compare if two solar panel components are equal.

        Parameters:
        - other (SolarPanel): The other solar panel to compare.

        Returns:
        - bool: True if the solar panels are equal, False otherwise.
        '''
        return isinstance(other, SolarPanel) and \
            self.name == other.name and \
            self.voltage == other.voltage and \
            self.current_mA == other.current_mA and \
            self.price == other.price
    

    def __hash__(self):
        '''
        Hash function

        Returns:
        - Hashing of name
        '''
        return hash(self.name)
    
    def display_user_friendly(self) -> str:
        '''Display the solar panel in a user-friendly format.'''
        return f"{self.voltage}V {self.current_mA}mA {self.name} ${self.price:.2f}"

    def display_csv(self) -> str:
        '''Display the solar panel as a CSV string.'''
        return f"{self.name},{self.voltage},{self.current_mA},{self.price:.2f}"
