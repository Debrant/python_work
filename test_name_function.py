import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests name_function.py with a double name"""
    def test_first_last_name(self):
        """Does the name come back formatted/"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        
    def test_middle_name(self):
        """Test Tests name_function.py with a tripple name"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')
        
unittest.main()
