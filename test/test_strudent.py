import unittest
from class_definitions import Student as s

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('Doe', 'John', 'Space Exploration', 3.7)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.first_name, "John")
        self.assertEqual(self.student.last_name, "Doe")
        self.assertEqual(self.student.major, "Space Exploration")

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student.first_name, "John")
        self.assertEqual(self.student.last_name, "Doe")
        self.assertEqual(self.student.major, "Space Exploration")
        self.assertEqual(self.student.gpa, 3.7)







if __name__ == '__main__':
    unittest.main()
