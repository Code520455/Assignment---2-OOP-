# File: validation.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: This file will help to validate all the data.
# This is my own work as defined by the Academic Integrity Policy


#---Rahul Saha---
from typing import List

def str_input(text: str, options: List[str] = []) -> str:
    '''
    Get a valid string input from the user.

    Parameters:
    - text (str): The prompt text for input.
    - options (List[str]): List of valid options (case-insensitive).

    Returns:
    - str: The user input.
    '''
    while True:
        inp = input(text)

        if inp.lower() not in [option.lower() for option in options]:
            print(f"Wrong input, must be a value from {options}")
            continue
        return inp
    
def int_input(text: str, start: int = 0, end: int = 100_000_000) -> int:
    '''
    Get a valid integer input from the user within a specified range.
    
    Parameters:
    - text (str): The prompt text for input.
    - start (int): The minimum allowed value.
    - end (int): The maximum allowed value.

    Returns:
    - int: The user input.
    '''
    while True:
        inp = input(text)

        if is_int(inp) and start <= int(inp) <= end:
            return int(inp)
        print(f"Wrong input, must be a number between {start} and {end}")


def float_input(text: str, start: float = 0.0, end: float = 100_000_000.0) -> float:
    '''
    Get a valid float input from the user within a specified range.

    Parameters:
    - text (str): The prompt text for input.
    - start (float): The minimum allowed value.
    - end (float): The maximum allowed value.

    Returns:
    - float: The user input.
    '''
    while True:
        inp = input(text)

        if is_float(inp) and start <= float(inp) <= end:
            return float(inp)
        print(f"Wrong input, must be a number between {start} and {end}")


def is_int(value: str) -> bool:
    '''
    Check if a given string can be converted to an integer.

    Parameters:
    - value (str): The input string.

    Returns:
    - bool: True if the string can be converted to an integer, False otherwise.
    '''
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_float(value: str) -> bool:
    '''
    Check if a given string can be converted to a float.

    Parameters:
    - value (str): The input string.

    Returns:
    - bool: True if the string can be converted to a float, False otherwise.
    '''
    try:
        float(value)
        return True
    except ValueError:
        return False
