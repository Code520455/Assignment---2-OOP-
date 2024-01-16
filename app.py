# File: app.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: This is the main application where user can do whatever they want. 
# This is my own work as defined by the Academic Integrity Policy

from validation import *
from file_handler import *
from light_kit import LightCircuitKit
from circuit_kit import CircuitKit
from sensor_kit import SensorCircuitKit
from typing import Optional

class App:
    def __init__(self):
        self.comments = load_circuits_data()
        self.circuit_kits : List[CircuitKit] = load_kit_data()
        self.home_menu_input()

    def home_menu_input(self):
        while True:
            print("\nHOME MENU")
            print("1. COMPONENTS")
            print("2. CIRCUIT KITS")
            print("3. CLOSE") 

            choice = int_input("Please enter a number: ",1,3)
            if choice == 1:
                self.component_menu()
            elif choice == 2:
                self.circuit_kits_menu()
            else:
                save_circuits_data(self.components)
                save_kit_data(self.circuit_kits)
                print("Data saved to File")

    def component_menu(self):
        while True:
            print("n\COMPONENT MENU")
            print("1. NEW COMPONENT") 
            print("2. VIEW COMPONENT")
            print("3. BACK")
            choice = int_input("Please enter a number:", 1, 3)
            if choice == 1:
                self.new_component_menu()
            elif choice == 2:
                self.view_components()
            else:
                return
             
    def new_component_menu(self):
        while True:
            print("\nNEW COMPONENT MENU")
            print("1. WIRE")
            print("2. BATTERY")
            print("3. SOLAR PANEL")
            print("4. LIGHT GLOBE")
            print("5. LED LIGHT")
            print("6. SWITCH")
            print("7. SENSOR")
            print("8. BUZZER")
            print("9. BACK")  
            
            choice = int_input("Please enter a number:", 1, 9)
            new_component = None
            if choice == 1:
                new_component = self.add_wire()
            elif choice == 2:
                new_component = self.add_battery()
            elif choice == 3:
                new_component = self.add_solar_panel()
            elif choice == 4:
                new_component = self.add_light_globe()
            elif choice == 5:
                new_component = self.add_led_light()
            elif choice == 6:
                new_component = self.add_switch()
            elif choice == 7:
                new_component = self.add_sensor()
            elif choice == 8:
                new_component = self.add_buzzer()
            else:
                return
