import unittest
from city_functions import get_city_listing


class TestCitiesListing(unittest.TestCase):
    """Tests city_functions.py with a city, country and population"""
    def test_city_listing_full(self):
        """Does the name come back formatted/"""
        withpop = get_city_listing('santiago', 'chile', population=6300000)
        self.assertEqual(withpop, 'Santiago, Chile, Population: 6300000')
        
    def test_city_listing_nopop(self):
        """ests city_functions.py with a city, country only"""
        nopop = get_city_listing('punta arenas', 'chile')
        self.assertEqual(nopop,'Punta Arenas, Chile')
        
unittest.main()
