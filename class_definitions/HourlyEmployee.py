"""
Morgan Christensen

Module 11 Polymorohism upadted employee class so that the hourly
and salary jobs are their own object

11/9/20
"""
from datetime import date

from class_definitions.employee2 import Employee


class HourlyEmployee(Employee):
    def __init__(self, lname, fname, phone, start_date, hourly_pay):
        super().__init__(lname, fname, phone)
        self.start_date = start_date
        self.hourly_pay = hourly_pay

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def hourly_pay(self):
        return self._hourly_pay

    @hourly_pay.setter
    def hourly_pay(self, value):
        if not isinstance(value, float):
            raise ValueError("Pay must be type float/decimal")
        self._hourly_pay = value

    def give_raise(self, value):
        if value <= self.hourly_pay:
            raise ValueError("pay rate needs to be greater than current pay")
        self.hourly_pay = value

    def display(self):
        return Employee.display(self) + ", " + str(self.start_date) + ", $" + str(self.hourly_pay) + "/hr"


#Driver
try:
    employee = HourlyEmployee("Christensen", "Morgan", "712-304-5478", date.today(), 10.00)
    print(employee.display())
    employee.give_raise(12.00)
    print(employee.display())
    del employee
except ValueError as err:
    print(err)