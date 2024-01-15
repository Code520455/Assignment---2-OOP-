 # File: sensor.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: sensor class
# This is my own work as defined by the Academic Integrity Policy

from input_component import InputComponent

class Sensor(InputComponent):
    '''
    Class representing a sensor. This class is a subclass of InputComponent.

    Attributes:
    - name (str): The name of the sensor.
    - price (float): The price of the sensor in dollars and cents.
    - voltage (float): The voltage of the sensor in volts.
    - sensor_type (str): The type of the sensor (e.g., movement, infrared, light, temperature, humidity, sound, dust).

    Author: Rajeswari Roy
    '''

    sensor_types = ["light", "motion", "infrared", "sound", "touch", "dust", "temperature", "humidity"]

    def __init__(self, name: str, price: float, voltage: float, sensor_type: str):
        super().__init__(name, price, voltage)
        self._sensor_type = sensor_type



    @property
    def sensor_type(self):
        return self._sensor_type

    @sensor_type.setter
    def sensor_type(self, value):
        self._sensor_type = value

    def duplicate(self) -> 'Sensor':
        '''Create a duplicate copy of the sensor.'''
        return Sensor(self.name, self.price, self.voltage, self.input_type)

    def parse_csv(self, csv_string: str) -> 'Sensor':
        '''
        Parse a CSV string to recreate a sensor object.

        Parameters:
        - csv_string (str): The CSV string containing sensor information.

        Returns:
        - Sensor: A new sensor object.
        '''
        name, price, voltage, sensor_type = csv_string.split(',')
        return Sensor(name, float(price), float(voltage), sensor_type)

    def __eq__(self, other: 'Sensor') -> bool:
        '''
        Compare if two sensor components are equal.

        Parameters:
        - other (Sensor): The other sensor to compare.

        Returns:
        - bool: True if the sensors are equal, False otherwise.
        '''
        return isinstance(other, Sensor) and \
            self.name == other.name and \
            self.price == other.price and \
            self.voltage == other.voltage and \
            self.input_type == other.input_type

    def __hash__(self):
        '''
        Hash function

        Returns:
        - Hashing of name
        '''
        return hash(self.name)

    def display_user_friendly(self) -> str:
        '''Display the sensor in a user-friendly format.'''
        return f"{self.voltage}V {self.input_type} {self.name} ${self.price:.2f}"

    def display_csv(self) -> str:
        '''Display the sensor as a CSV string.'''
        return f"{self.name},{self.input_type},{self.voltage},{self.price:.2f}"
