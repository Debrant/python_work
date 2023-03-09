from unittest import mock
from unittest import TestCase
import unittest
from employee import Employee

class TestEmployeeRaise(unittest.TestCase):
    """A test class for my employee class."""
    
    def setUp(self):
        """Set test variables."""
        annual_raise = 15001
        self.test_employee = Employee('johan sebastian bach', 99150)
        
        
        
    def test_give_default_raise(self):
        """Test that 5000 is add correctly if no custom ammount is passed"""
        self.test_employee.give_raise()
        self.assertEqual(self.test_employee.salary, 104150)
        
    def test_give_custom_raise(self):
        """Test that a custom raise is reflected in salary."""
        self.test_employee.give_raise(10850)
        self.assertEqual(self.test_employee.salary, 110000)
        
        
class TestEmployeeWageUpdate(unittest.TestCase):
    @mock.patch('Employee.update_salary.input', create=True)    
    # def test_update_salary(self, mocked_input):
        # """Test update salary function."""
        # update_salary.side_effect = ['n', 120000, 'y']
        # self.assertEqual(self.test_employee.salary, 120000)
        
        
        
        
unittest.main()
