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
    components = {}

    try:
        with open(FILE_NAME, 'r') as file:
            for line in file.readlines():
                words = line.strip().split(",")
                component = None
                quantity = int(words[0])
                component_type = words[1]
                if component_type == "Wire":
                    length = float(words[2])
                    price = float(words[3])
                    component = Wire(component_type, length, price)

                elif component_type == "Solar Panel":
                    voltage = float(words[2])
                    current = float(words[3])
                    price = float(words[4])
                    component = SolarPanel(component_type, voltage, current, price)

                elif component_type == "Battery":
                    size = words[2]
                    volatge = float(words[3])
                    price = float(words[4])
                    component = Battery(component_type, size, voltage, price)

                elif component_type == "Switch" or component_type == "Sensor":
                    s_type = words[2]
                    voltage = float(words[3])
                    price = float(words[4])
                    if component_type == "Switch":
                        component = Switch(component_type, price, voltage, s_type)
                    else:
                        component = Sensor(component_type, price, voltage, s_type)
                elif component_type == "LED Light" or component_type == "Light Globe":
                    color = words[2]
                    voltage = float(words[3])
                    current = int(words[4])
                    price = float(words[5])
                    if component_type == "LED Light":
                        component = LEDLight(component_type, price, voltage, current, color)
                    else:
                        component = LightGlobe(component_type, price, voltage, current, color)
                elif component_type == "Buzzer":
                    freq = int(words[2])
                    db = int(words[3])
                    voltage = float(words[4])
                    current = int(words[5])
                    price = float(words[6])
                    component = Buzzer(component_type, price, voltage, current, freq, db)
                components[component] = quantity
            file.close()
            return components

    except FileNotFoundError:
        print("File not found: circuits.csv")
    except Exception as e:
        print(f"An error occurred while loading data: {e}")

def save_data(components: Dict[Component, int]) -> None:
    '''
    Save data to the circuits.csv file.

    Parameters:
    - components (Dict[Component, int]): A dictionary where keys are Component objects and values are their quantities.
    '''
    try:
        with open(FILE_NAME, "w") as file:
            for component, quantity in components.items():
                csv_string = component.display_csv()
                file.write(f"{quantity},{csv_string}\n")
            file.close()
    except Exception as e:
        print(f"An error occurred while saving data to file: {e}")

