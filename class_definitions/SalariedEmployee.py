"""
Morgan Christensen

Module 11 Polymorohism upadted employee class so that the hourly
and salary jobs are their own object

11/9/20
"""
from datetime import date

from class_definitions.employee2 import Employee


class SalariedEmployee(Employee):
    def __init__(self, lname, fname, phone, start_date, salary):
        super().__init__(lname, fname, phone)
        self.start_date = start_date
        self.salary = salary

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, float):
            raise ValueError("Pay must be type float/decimal")
        self._salary = value

    def give_raise(self, value):
        if value <= self.salary:
            raise ValueError("pay rate needs to be greater than current pay")
        self.salary = value

    def display(self):
        return Employee.display(self) + ", " + str(self.start_date) + ", $" + str(self.salary) + "/month"


# Driver
try:
    employee = SalariedEmployee("Christensen", "Morgan", "712-304-5478", date.today(), 3500.00)
    print(employee.display())
    employee.give_raise(4000.00)
    print(employee.display())
    del employee
except ValueError as err:
    print(err)
