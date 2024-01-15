# File: validation.py
# Author: RAHUL SAHA
# ID: 520455
# Email: 520455@learning.eynesbury.edu.au
# Author: Rajeswari Roy
# ID: 520456
# Email: 520456@learning.eynesbury.edu.au
# Description: This file will help to validate all the data.
# This is my own work as defined by the Academic Integrity Policy


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