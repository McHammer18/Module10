import unittest
from class_definitions import Student as s

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student1 = s.Student('Doe', 'John', 'Space Exploration')
        self.student2 = s.Student('Doe', 'John', 'Space Exploration', 3.7)

    def tearDown(self):
        del self.student1
        del self.student2

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student1.first_name, "John")
        self.assertEqual(self.student1.last_name, "Doe")
        self.assertEqual(self.student1.major, "Space Exploration")
        self.assertEqual(self.student1.gpa, 0.0)

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student2.first_name, "John")
        self.assertEqual(self.student2.last_name, "Doe")
        self.assertEqual(self.student2.major, "Space Exploration")
        self.assertEqual(self.student2.gpa, 3.7)

    def test_student_str(self):
        self.assertEqual(str(self.student2), "Doe, John has major Space Exploration with gpa: 3.7")







if __name__ == '__main__':
    unittest.main()
