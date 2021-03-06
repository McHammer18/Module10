import unittest
from class_definitions import Student as s

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student1 = s.Student('Doe', 'John', 'Criminal Justice')
        self.student2 = s.Student('Doe', 'John', 'Criminal Justice', 3.7)

    def tearDown(self):
        del self.student1
        del self.student2

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student1.first_name, "John")
        self.assertEqual(self.student1.last_name, "Doe")
        self.assertEqual(self.student1.major, "Criminal Justice")
        self.assertEqual(self.student1.gpa, 0.0)

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student2.first_name, "John")
        self.assertEqual(self.student2.last_name, "Doe")
        self.assertEqual(self.student2.major, "Criminal Justice")
        self.assertEqual(self.student2.gpa, 3.7)

    def test_student_str(self):
        self.assertEqual(str(self.student2), "Doe, John has major Criminal Justice with gpa: 3.7")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            stu = s.Student("Ch1rst3ns3n", "Moragan", "Cybersecurity", 3.8)

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            stu = s.Student("Chirstensen", "M0rg8n", "Cybersecurity", 3.8)

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            stu = s.Student("Chirstensen", "M0rg8n", "World Domination", 3.8)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            stu = s.Student("Chirstensen", "M0rg8n", "Cybersecurity", 3.8)




if __name__ == '__main__':
    unittest.main()
