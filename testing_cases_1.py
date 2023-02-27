import unittest
from get_formatted_name import get_formatted_name

class NameTestCases(unittest.TestCase):
    """Testing for get_formatted_name() function"""
    def test_first_last(self):
        """Will "Anurag Pareek" valid !!"""
        formatted_name = get_formatted_name("Anurag","Pareek")
        self.assertEqual(formatted_name,"Anurag Pareek")
    def test_first_middle_last(self):
        """Will "Anurag Pareek  : Name" valid !!""" 
        formatted_name_1 = get_formatted_name("Anurag"," : Name","Pareek")
        self.assertEqual(formatted_name_1,"Anurag Pareek  : Name")
unittest.main()
