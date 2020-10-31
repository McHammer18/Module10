import unittest
from class_definitions import Student as s

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('Doe', 'John', 'Space exploration')

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.first_name, "John")
        self.assertEqual(self.student.last_name, "Doe")
        self.assertEqual(self.student.major, "Space exploration")





if __name__ == '__main__':
    unittest.main()
