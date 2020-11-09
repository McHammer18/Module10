"""
Morgan Christensen

Module 10: unit testing classes

10/31/20
"""
from class_definitions.Person import Person


class Student(Person):
    """Student class"""
    MAJORS = ('Liberal Arts', 'Comp Science', 'Math', 'Computer Engineering', 'English', 'Criminal Justice', 'Cybersecurity', 'Being Awesome!')
    def __init__(self, s_id, lname, fname, major='Math', gpa=0.0):
        if major not in self.MAJORS:
            raise ValueError("not a valid major")
        super().__init__(fname, lname)
        self._s_id = s_id
        self._major = major
        self._gpa = gpa

    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, value):
        if not isinstance(value, float):
            raise ValueError("Not a valid gpa float value")
        if not 0.0 <= value <= 4.0:
            raise ValueError("Not a valid gpa range")
        self._gpa = value

    def display(self):
        return Person.display(self) + " (" + str(self._s_id) + ") " + self._major + " gpa: " + str(self._gpa)

    def change_major(self, major):
        self._major = major

    def change_gpa(self, gpa=0.0):
        self.gpa = gpa


#Driver
my_student = Student(900111111, 'Song', 'River')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())
del my_student
