import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):

    """ Test for name_function.py """

    def test_first_last_name(self):
        """ Names like 'Janis Joplin works? """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """ Names like 'Wolfang Amadeus Mozart works? """
        formatted_name = get_formatted_name('wolfang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfang Amadeus Mozart')


unittest.main()