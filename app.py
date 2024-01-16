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
        self.components = load_circuits_data()
        self.circuit_kits: List[CircuitKit] = load_kit_data()
        self.home_menu_input()

    def home_menu_input(self):
        while True:
            print("\nHOME MENU")
            print("1. COMPONENTS")
            print("2. CIRCUIT KITS")
            print("3. CLOSE")

            choice = int_input("Please enter a number:", 1, 3)
            if choice == 1:
                self.component_menu()
            elif choice == 2:
                self.circuit_kits_menu()
            else:
                save_circuits_data(self.components)
                save_kit_data(self.circuit_kits)
                print("Data Saved to File")
                return

    def component_menu(self):
        while True:
            print("\nCOMPONENT MENU")
            print("1. NEW COMPONENT")
            print("2. VIEW COMPONENTS")
            print("3. BACK")

            choice = int_input("Please enter a number:", 1, 3)
            if choice == 1:
                self.new_component_menu()
            elif choice == 2:
                self.view_components()
            else:
                return

    def circuit_kits_menu(self):
        while True:
            print("\nCIRCUIT KIT MENU")
            print("1. NEW CIRCUIT KIT")
            print("2. VIEW CIRCUIT KITS")
            print("3. BACK")

            choice = int_input("Please enter a number:", 1, 3)
            if choice == 1:
                self.new_circuit_kit_menu()
            elif choice == 2:
                self.view_circuit_kits()
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

            component = new_component[0]
            num = new_component[1]

            self.components[component] = num
            print(f"Added {component.display_user_friendly()} X {num}")

    def view_components(self):
        while True:
            print("ALL COMPONENTS")
            i = 1
            for key, value in self.components.items():
                print(f"{i}. {key.display_user_friendly()} X {value}")
                i += 1
            print(f"{i}. BACK")

            choice = int_input("Please enter a number:", 1, i)
            if choice == i:
                return
            self.buy_sell_component(choice - 1)

    def buy_sell_component(self, component_number: int):

        component, num = list(self.components.items())[component_number]
        while True:
            print(component.display_user_friendly())
            print("1. BUY")
            print("2. SELL")
            print("3. BACK")
            choice = int_input("Please enter a number: ", 1, 3)

            if choice == 1:
                print(f"Buying {component.display_user_friendly()}")
                number_add = int_input(f"Please enter number of {component.display_user_friendly()}: ")
                self.components[component] += number_add
                print(f"Bought {component.display_user_friendly()} X {number_add}")
            elif choice == 2:
                print(f"Selling {component.display_user_friendly()}")
                number_sold = int_input(f"Please enter number of {component.display_user_friendly()}: ",
                                        1, self.components[component])
                self.components[component] -= number_sold
                print(f"Sold {component.display_user_friendly()} X {number_sold}")
            else:
                return

    def add_wire(self) -> tuple:
        print("NEW WIRE")
        length = float_input("Please enter length (mm): ")
        price = float_input("Please enter price: ")
        num = int_input("Please enter number of Wires: ")
        wire = Wire("Wire", length, price)

        return wire, num

    def add_battery(self) -> tuple:
        print("NEW BATTERY")
        print("Battery sizes are AA or AAA or C or D or E")
        size = str_input("Please enter battery size:", Battery.battery_sizes)
        print("AA, AAA and C batteries are either 1.2 Volts or 1.5 Volts")
        print("D batteries are 1.5 Volts")
        print("E batteries are 9.0 Volts")
        voltage = float_input("Please enter a voltage that matches the battery size: ")
        price = float_input("Please enter price: ")
        num = int_input("Please enter number of Batteries: ")
        battery = Battery("Battery", size, voltage, price)

        return battery, num

    def add_solar_panel(self) -> tuple:
        print("NEW SOLAR PANEL")
        print("Voltage is usually between 1 and 12")
        voltage = float_input("Please enter voltage (V): ", 1, 12)
        print("Current is usually between 100 and 1000 milliAmps")
        current = float_input("Please enter current (mA): ", 100, 1000)
        price = float_input("Please enter price: ")
        num = int_input("Please enter number of Solar Panels: ")
        solar_panel = SolarPanel("Solar Panel", voltage, current, price)

        return solar_panel, num

    def add_light_globe(self) -> tuple:
        print("NEW LIGHT GLOBE")
        print("Light Globe Colours:\nwarm, neutral, cool")
        color = str_input("Please enter light globe colour: ", LightGlobe.light_globe_colors)
        print("Voltage is usually between 1 and 12")
        voltage = float_input("Please enter voltage (V): ", 1, 12)
        print("Current is usually between 100 and 1000 milliAmps")
        current = float_input("Please enter current (mA): ", 100, 1000)
        price = float_input("Please enter price: ")
        num = int_input("Please enter number of Light Globes: ")
        light_globe = LightGlobe("Light", price, voltage, current, color)

        return light_globe, num

    def add_led_light(self) -> tuple:
        print("NEW LED LIGHT")
        print("LED Light Colours:\nwhite, red, green, blue, yellow, orange, pink, aqua, violet")
        color = str_input("Please enter LED light colour: ", LEDLight.led_light_colors)
        print("Voltage is usually between 1 and 12")
        voltage = float_input("Please enter voltage (V): ", 1, 12)
        print("Current is usually between 100 and 1000 milliAmps")
        current = float_input("Please enter current (mA): ", 100, 1000)
        price = float_input("Please enter price: ")
        num = int_input("Please enter number of LED lights: ")
        led_light = LEDLight("Light", price, voltage, current, color)

        return led_light, num

    def add_switch(self) -> tuple:
        print("NEW SWITCH")
        print("Switch types:\npush, slide, rocker, toggle")
        type_switch = str_input("Please enter switch type: ", Switch.switch_types)
        print("Voltage is usually between 1 and 12")
        voltage = float_input("Please enter voltage (V): ", 1, 12)
        price = float_input("Please enter price: ")
        num = int_input("Please enter number of Switches: ")
        switch = Switch("Switch", price, voltage, type_switch)

        return switch, num

    def add_sensor(self) -> tuple:
        print("NEW SENSOR")
        print("Sensor types:\nlight, motion, infrared, sound, touch, dust, temperature,humidity")
        type_sensor = str_input("please enter sensor type: ", Sensor.sensor_types)
        print("Voltage is usually between 1 and 12")
        voltage = float_input("Please enter voltage (V): ", 1, 12)
        price = float_input("Please enter price: ")
        num = int_input("Please enter number of Sensors: ")
        sensor = Sensor("Sensor", price, voltage, type_sensor)

        return sensor, num

    def add_buzzer(self) -> tuple:
        print("NEW BUZZER")
        freq = int_input("Please enter frequency (Hz): ")
        db = int_input("Please enter sound pressure (dB): ")
        print("Voltage is usually between 1 and 12")
        voltage = float_input("Please enter voltage (V): ", 1, 12)
        print("Current is usually between 100 and 1000 milliAmps")
        current = float_input("Please enter current (mA): ", 100, 1000)
        price = float_input("Please enter price: ")
        num = int_input("Please enter number of Buzzers: ")
        buzzer = Buzzer("Buzzer", price, voltage, current, freq, db)

        return buzzer, num

    def new_circuit_kit_menu(self):
        while True:
            print("\nNEW CIRCUIT KIT MENU")
            print("1. LIGHT GLOBE CIRCUIT KIT")
            print("2. LED LIGHT CIRCUIT KIT")
            print("3. SENSOR CIRCUIT KIT WITH LIGHT GLOBE")
            print("4. SENSOR CIRCUIT KIT WITH LED LIGHT")
            print("5. SENSOR CIRCUIT KIT WITH BUZZER")
            print("6. SENSOR CIRCUIT KIT WITH LIGHT GLOBE AND SWITH")
            print("7. SENSOR CIRCUIT KIT WITH LED LIGHT AND SWITCH")
            print("8. SENSOR CIRCUIT KIT WITH BUZZER AND SWITCH")
            print("9. BACK")

            choice = int_input("Please enter a number:", 1, 9)
            new_circuit_kit = None
            if choice == 1:
                self.add_light_circuit_kit("Light Globe")
            elif choice == 2:
                self.add_light_circuit_kit("LED Light")
            elif choice == 3:
                self.add_sensor_circuit_kit(False, "Light Globe")
            elif choice == 4:
                self.add_sensor_circuit_kit(False, "LED Light")
            elif choice == 5:
                self.add_sensor_circuit_kit(False, "Buzzer")
            elif choice == 6:
                self.add_sensor_circuit_kit(True, "Light Globe")
            elif choice == 7:
                self.add_sensor_circuit_kit(True, "LED Light")
            elif choice == 8:
                self.add_sensor_circuit_kit(True, "Buzzer")
            else:
                return

    def add_light_circuit_kit(self, light_type: str):
        print(f"{light_type.upper()} CIRCUIT KIT")
        light = self.component_input(light_type)
        print(f"Selecting {light.display_user_friendly()}")
        light_num = int_input(f"Please enter number of {light.display_user_friendly()}: ", 1,
                              self.components[light])
        print("Select type of switch")
        switch = self.component_input("Switch")
        print(f"Selecting {switch.display_user_friendly()}")
        switch_num = int_input(f"Please enter number of {switch.display_user_friendly()}: ",
                               1, self.components[switch])
        battery = self.component_input("Battery")
        print(f"Selecting {battery.display_user_friendly()}")
        battery_num = int_input(f"Please enter number of {battery.display_user_friendly()}: ",
                                1, self.components[battery])
        wire = self.component_input("Wire")
        print(f"Selecting {wire.display_user_friendly()}")
        wire_num = int_input(f"Please enter number of {wire.display_user_friendly()}: ",
                             1, self.components[wire])

        light_info = (light, light_num)
        switch_info = (switch, switch_num)
        battery_info = (battery, battery_num)
        wire_info = (wire, wire_num)
        # remove amount of components from components dict
        self.components[light] -= light_num
        self.components[switch] -= switch_num
        self.components[battery] -= battery_num
        self.components[wire] -= wire_num
        kit = LightCircuitKit(light_type, 1, light_info, switch_info, battery_info, wire_info)

        self.circuit_kits.append(kit)
        print(f"Added {kit.display_details()}")

    def add_sensor_circuit_kit(self, needSwitch: bool, output_type: str):
        print("SENSOR CIRCUIT TYPE", end=" ")
        print("WITH", output_type, end=" ")
        if needSwitch:
            print("AND SWITCH")
        sensor = self.component_input("Sensor")
        print(f"Selecting {sensor.display_user_friendly()}")
        print(f"Select type of {output_type}")
        output_component = self.component_input(output_type)
        print(f"Selecting {output_component.display_user_friendly()}")
        power_source = self.component_input("Power Supply", "Battery")
        print(f"Selecting {power_source.display_user_friendly()}")
        source_num = int_input(f"Please enter number of {power_source.display_user_friendly()}: ", 1,
                               self.components[power_source])
        switch = None
        if needSwitch:
            switch = self.component_input("Switch")
            print(f"Selecting {switch.display_user_friendly()}")
        wire = self.component_input("Wire")
        print(f"Selecting {wire.display_user_friendly()}")
        wire_num = int_input(f"Please enter number of {wire.display_user_friendly()}: ",
                             1, self.components[wire])
        # remove amount of components from components dict
        self.components[sensor] -= 1
        self.components[output_component] -= 1
        self.components[power_source] -= source_num
        self.components[wire] -= wire_num
        if needSwitch:
            self.components[switch] -= 1
        kit = SensorCircuitKit("Sensor Circuit", 1, (power_source, source_num), sensor, output_component,
                               (wire, wire_num), switch)
        self.circuit_kits.append(kit)
        print(f"Added {kit.display_details()}")

    def view_circuit_kits(self):
        while True:
            print("ALL CIRCUIT KITS")
            i = 1
            for kit in self.circuit_kits:
                print(f"{i}. {kit.display_details()}")
                i += 1
            print(f"{i}. BACK")

            choice = int_input("Please enter a number:", 1, i)
            if choice == i:
                return
            self.sell_pack_unpack_circuit_kit(choice - 1)

    def sell_pack_unpack_circuit_kit(self, circuit_kit_number: int):
        circuit_kit = self.circuit_kits[circuit_kit_number]
        while True:
            print(f"\n{circuit_kit.display_details()}")
            print("1. SELL")
            print("2. PACK")
            print("3. UNPACK")
            print("4. BACK")
            choice = int_input("Please enter a number: ", 1, 5)

            if choice == 1:
                print(f"Selling {circuit_kit.display_details()}")
                number_sold = int_input(f"Please enter number of {circuit_kit.display_details()}: ",
                                        1, circuit_kit.count)
                print(f"Sold {circuit_kit.display_details()} X {number_sold}")
                circuit_kit.count -= number_sold
            elif choice == 2:
                print(f"Packing {circuit_kit.display_details()}")
                number_packed = int_input(f"Please enter number of {circuit_kit.display_details()}: ",
                                          1, circuit_kit.count)
                print(f"Packed {circuit_kit.display_details()} X {number_packed}")
                circuit_kit.count -= number_packed
            elif choice == 3:
                print(f"Unpacking {circuit_kit.display_details()}")
                number_unpacked = int_input(f"Please enter number of {circuit_kit.display_details()}: ")
                print(f"Unpacked {circuit_kit.display_details()} X {number_unpacked}")
                circuit_kit.count += number_unpacked
            else:
                return

    def component_input(self, component_type: str, component_type2: str = None) -> Component:
        data = self.get_component_by_type(component_type)
        if component_type2 is not None:
            data += self.get_component_by_type(component_type2)
        i = 0
        for i, val in enumerate(data):
            print(f"{i + 1} {val.display_user_friendly()} X {self.components[val]}")
        choice = int_input("Please select the component index:", 1, i + 1)
        component = data[choice - 1]
        return component

    def get_component_by_type(self, component_type: str) -> Optional[List[Component]]:
        data = []
        for key in self.components.keys():
            if key.name.lower() == component_type.lower():
                data.append(key)
        return data

App()

