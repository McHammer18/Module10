class Employee:
    """Employee class"""

    #Constructor
    def __init__(self, lname, fname, phone):
        self.last_name = lname
        self.first_name = fname
        self.phone = phone

    def display(self):
        return "Name: " + self.first_name + " " + self.last_name + "\nPhone: " + self.phone