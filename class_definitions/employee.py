"""
Morgan Christensen

Module 10: Encapsulation

10/27/20
"""
from datetime import date


class Employee:
    """Employee class"""

    #Constructor
    def __init__(self, lname, fname, phone):
        self.last_name = lname
        self.first_name = fname
        self.phone = phone

    def display(self):
        return "Name: " + self.first_name + " " + self.last_name + "\nPhone: " + self.phone