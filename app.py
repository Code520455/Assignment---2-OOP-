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
            
            