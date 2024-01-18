# File: battery.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: component class
# This is my own work as defined by the Academic Integrity Policy

#---Rahul Saha---
from power_supply import PowerSupply

class Battery(PowerSupply):
    '''
    Represents a battery component used as a power source.

    Attributes:
    - name (str): The name of the battery.
    - size (str): The size of the battery (e.g., AA, AAA).
    - voltage (float): The voltage of the battery in volts.
    - price (float): The price of the battery in dollars and cents.

    '''
    battery_sizes = ["AA", "AAA", "C", "D", "E"]
    battery_voltages = {
        1.2: ["AA", "AAA", "C"],
        1.5: ["D"],
        9.0: ["E"]
    }
    def __init__(self, name: str, size: str, voltage: float, price: float):
        super().__init__(name, price, voltage)
        self._size = size
        
    @property
    def size(self) -> str:
        '''Get the size of the battery'''
        return self._size
    
    @size.setter
    def size(self, value: str) -> None:
        '''Set the size of the battery.'''
        self._size = value

    def duplicate(self) -> 'Battery':
        '''Create a duplicate copy of the battery.'''
        return Battery(self.name, self.size, self.voltage, self.price)

    def parse_csv(self, csv_string: str) -> 'Battery':
        '''
        Parse a CSV string to recreate a battery object.

        Parameters:
        - csv_string (str): The CSV string containing battery information.

        Returns:
        - Battery: A new battery object.
        '''
        name, size, voltage, price = csv_string.split(',')
        return Battery(name, size, float(voltage), float(price))

    def __eq__(self, other: 'Battery') -> bool:
        '''
        Compare if two battery components are equal.

        Parameters:
        - other (Battery): The other battery to compare.

        Returns:
        - bool: True if the batteries are equal, False otherwise.
        '''
        return isinstance(other, Battery) and \
            self.name == other.name and \
            self.size == other.size and \
            self.voltage == other.voltage and \
            self.price == other.price

    def __hash__(self):
        '''
        Hash function

        Returns:
        - Hashing of name
        '''
        return hash(self.name)

    def display_user_friendly(self) -> str:
        '''Display the battery in a user-friendly format.'''
        return f"{self.voltage}V {self.size} {self.name} ${self.price:.2f}"

    def display_csv(self) -> str:
        '''Display the battery as a CSV string.'''
        return f"{self.name},{self.size},{self.voltage},{self.price:.2f}"
