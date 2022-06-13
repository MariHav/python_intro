import unittest
from city_functions import get_city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for cities function"""

    def test_cities(self):
        formatted_city_country = get_city_country('lviv','ukraine',500000)
        self.assertEqual(formatted_city_country, 'Lviv, Ukraine - population 500000')

if __name__== '__main__':
    unittest.main()
