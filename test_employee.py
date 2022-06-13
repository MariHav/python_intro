import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for class Employee"""

    def setUp(self):
        first_name = 'Jane'
        second_name = 'Lopez'
        salary = 100000
        self.new_employee = Employee(first_name,second_name,salary)

    def test_default_rise(self):
        """Test if default salary rise gives the correct amount of annual salary"""
        defaul_rise = self.new_employee.give_rise()
        self.assertEqual(defaul_rise,105000)

    def test_custom_rise(self):
        """Test if custom rise gives the correct amount of annual salary"""
        custom_rise = self.new_employee.give_rise(10000)
        self.assertEqual(custom_rise,110000)

if __name__ == '__main__':
    unittest.main()

