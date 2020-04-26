import unittest
from config import Config

api = Config.API_KEY
class Testt(unittest.TestCase):
    def test_env(self):
        self.assertEqual(api,'c266d77c61324626bad16a93d263ce58')
        



if __name__ =='__main__':
    unittest.main()

