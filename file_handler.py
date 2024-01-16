# File: file_handler.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: It will handle the other classes
# This is my own work as defined by the Academic Integrity Policy

from typing import Dict, Optional, List
from component import Component
from wire import Wire
from battery import Battery
from solar_panel import SolarPanel
from light_globe import LightGlobe
from led_light import LEDLight
from switch import Switch
from sensor import Sensor
from buzzer import Buzzer
from circuit_kit import CircuitKit
from light_kit import LightCircuitKit
from sensor_kit import SensorCircuitKit

CIRCUITS_FILE = "circuits.csv"
KITS_FILE = "components.csv"


def load_circuits_data() -> Dict[Component, int]:
    '''
    Load data from the circuits.csv file and return a dictionary of components with quantities.

    Returns:
    - Dict[Component, int]: A dictionary where keys are Component objects and values are their quantities.
    '''
    components = {}

    try:
        with open(CIRCUITS_FILE, "r") as file:
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
                    voltage = float(words[3])
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


def save_circuits_data(components: Dict[Component, int]) -> None:
    '''
    Save data to the circuits.csv file.

    Parameters:
    - components (Dict[Component, int]): A dictionary where keys are Component objects and values are their quantities.
    '''
    try:
        with open(CIRCUITS_FILE, "w") as file:
            for component, quantity in components.items():
                csv_string = component.display_csv()
                file.write(f"{quantity},{csv_string}\n")
            file.close()
    except Exception as e:
        print(f"An error occurred while saving data to file: {e}")


def load_kit_data() -> List[CircuitKit]:
    '''
    load data from components.csv
    
    Returns:
    - circuitKit: A dictionary of circuit kit
    '''
    data = []
    try:
        with open(KITS_FILE, "r") as file:
            for line in file.readlines():
                words = line.strip().split(",")
                quantity = int(words[0])
                kit = None
                kit_type = words[1]
                if kit_type.lower() == "Light Circuit".lower():
                    q = int(words[2])
                    # ignore 3rd index for Battery
                    size = words[4]
                    voltage = float(words[5])
                    price = float(words[6])
                    battery_info = (Battery("Battery", size, voltage, price), q)
                    q = int(words[7])
                    component_type = words[8]
                    color = words[9]
                    voltage = float(words[10])
                    current = int(words[11])
                    price = float(words[12])
                    light = None
                    if component_type.lower() == "LED Light".lower():
                        light = LEDLight(component_type, price, voltage, current, color)
                    else:
                        light = LightGlobe(component_type, price, voltage, current, color)
                    light_info = (light, q)
                    q = int(words[13])
                    length = float(words[15])
                    price = float(words[16])
                    wire_info = (Wire("Wire", length, price), q)
                    q = int(words[17])
                    # ignore 18th index for Switch
                    s_type = words[19]
                    voltage = float(words[20])
                    price = float(words[21])
                    switch_info = (Switch("Switch", price, voltage, s_type), q)
                    kit = LightCircuitKit(kit_type, quantity, light_info, switch_info, battery_info, wire_info)
                elif kit_type == "Sensor Circuit":
                    q = int(words[2])
                    power_type = words[3]
                    power_supply_info = None
                    if power_type == "Solar Panel":
                        voltage = float(words[4])
                        current = float(words[5])
                        price = float(words[6])
                        power_supply_info = (SolarPanel("Solar Panel", voltage, current, price), q)
                    elif power_type == "Battery":
                        size = words[4]
                        voltage = float(words[5])
                        price = float(words[6])
                        power_supply_info = (Battery("Battery", size, voltage, price), q)
                    q = int(words[7])
                    output_type = words[8]
                    output_component = None
                    next_index = -1
                    if output_type == "Buzzer":
                        freq = int(words[9])
                        db = int(words[10])
                        voltage = float(words[11])
                        current = int(words[12])
                        price = float(words[13])
                        next_index = 14
                        output_component = Buzzer(output_type, price, voltage, current, freq, db)
                    elif output_type == "Light Globe" or output_type == "LED Light":
                        color = words[9]
                        voltage = float(words[10])
                        current = int(words[11])
                        price = float(words[12])
                        next_index = 13
                        if output_type == "LED Light":
                            output_component = LEDLight(output_type, price, voltage, current, color)
                        else:
                            output_component = LightGlobe(output_type, price, voltage, current, color)
                    q = int(words[next_index])
                    sensor_type = words[next_index + 2] #ignore 15th index for Sensor
                    voltage = float(words[next_index + 3])
                    price = float(words[next_index + 4])
                    sensor = Sensor(sensor_type, price, voltage, sensor_type)
                    q = int(words[next_index + 5])
                    length = float(words[next_index + 7])
                    price = float(words[next_index + 8])
                    wire_info = (Wire("Wire", length, price), q)
                    # if next index exists
                    if len(words) > next_index + 9:
                        q = int(words[next_index + 9])
                        s_type = words[next_index + 11]
                        voltage = float(words[next_index + 12])
                        price = float(words[next_index + 13])
                        switch = Switch("Switch", price, voltage, s_type)
                        kit = SensorCircuitKit(kit_type, quantity, power_supply_info, sensor, output_component, wire_info, switch)
                    else:
                        kit = SensorCircuitKit(kit_type, quantity, power_supply_info, sensor, output_component, wire_info)

                data.append(kit)
        return data
    except FileNotFoundError:
        print("File not found: circuits.csv")
    except Exception as e:
        print(f"An error occurred while loading data: {e}")


def save_kit_data(kits: List[CircuitKit]) -> None:
    '''
    save data into components.csv
    
    Parameters:
    - kits: A dictionary of circuit kit
    '''
    try:
        with open(KITS_FILE, "w") as file:
            for kit in kits:
                csv_string = kit.display_csv()
                file.write(f"{csv_string}\n")
            file.close()
    except Exception as e:
        print(f"An error occurred while saving data to file: {e}")
