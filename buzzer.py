# File: buzzer.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: component class
# This is my own work as defined by the Academic Integrity Policy



from output_component import OutputComponent


class Buzzer(OutputComponent):
    '''
    Class representing a buzzer. This class is a subclass of OutputComponent.

    Attributes:
    - name (str): The name of the buzzer.
    - price (float): The price of the buzzer in dollars and cents.
    - voltage (float): The voltage of the buzzer in volts.
    - current (float): The current of the buzzer in milliamps.
    - frequency (float): The frequency of the buzzer in Hertz.
    - sound_pressure (float): The sound pressure of the buzzer in decibels.

    Author: Rajeswari Roy
    '''

    def __init__(self, name: str, price: float, voltage: float, current_mA: float, frequency: float,
                 sound_pressure: float):
        super().__init__(name, price, voltage, current_mA)
        self._frequency = frequency
        self._sound_pressure = sound_pressure

    @property
    def frequency(self) -> float:
        '''Get the frequency of the buzzer.'''
        return self._frequency

    @frequency.setter
    def frequency(self, value: float) -> None:
        '''Set the frequency of the buzzer.'''
        self._frequency = value

    @property
    def sound_pressure(self) -> float:
        '''Get the sound pressure of the buzzer.'''
        return self._sound_pressure

    @sound_pressure.setter
    def sound_pressure(self, value: float) -> None:
        '''Set the sound pressure of the buzzer.'''
        self._sound_pressure = value

    def duplicate(self) -> 'Buzzer':
        '''Create a duplicate copy of the buzzer.'''
        return Buzzer(self.name, self.price, self.voltage, self.current, self.frequency, self.sound_pressure)

    def parse_csv(self, csv_string: str) -> 'Buzzer':
        '''
        Parse a CSV string to recreate a buzzer object.

        Parameters:
        - csv_string (str): The CSV string containing buzzer information.

        Returns:
        - Buzzer: A new buzzer object.
        '''
        name, price, voltage, current, frequency, sound_pressure = csv_string.split(',')
        return Buzzer(name, float(price), float(voltage), float(current), float(frequency), float(sound_pressure))

    def __eq__(self, other: 'Buzzer') -> bool:
        '''
        Compare if two buzzer components are equal.

        Parameters:
        - other (Buzzer): The other buzzer to compare.

        Returns:
        - bool: True if the buzzers are equal, False otherwise.
        '''
        return isinstance(other, Buzzer) and \
            self.name == other.name and \
            self.price == other.price and \
            self.voltage == other.voltage and \
            self.current == other.current and \
            self.frequency == other.frequency and \
            self.sound_pressure == other.sound_pressure

    def __hash__(self):
        '''
        Hash function

        Returns:
        - Hashing of name
        '''
        return hash(self.name)

    def display_user_friendly(self) -> str:
        '''Display the buzzer in a user-friendly format.'''
        return f"{self.voltage}V {self.current}mA {self.frequency}Hz {self.sound_pressure}dB {self.name} Price: ${self.price:.2f}"

    def display_csv(self) -> str:
        '''Display the buzzer as a CSV string.'''
        return f"{self.name},{self.frequency},{self.sound_pressure},{self.voltage},{self.current},{self.price:.2f}"
