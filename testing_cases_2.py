import unittest
from city_function import city_functions

class TestingCityCountryCases(unittest.TestCase):
    """"""
    def test_city_country(self):
        """"""
        test = city_functions("Guwahati","India")
        self.assertEqual(test,"Guwahati, India")
    
    def test_city_country_population(self):
        """"""
        test_1 = city_functions("Guwahati","Assam","*****")
        self.assertEqual(test_1,"Guwahati, Assam - *****")
unittest.main()