import unittest
from app.models import NewsSourceModel

class TestNewsSource(unittest.TestCase):
    def setUp(self):
        '''
        Setup method that will be run before every test
        '''
        self.new_source = NewsSourceModel(1,'name','description','url','category','language','country')

    def test_init(self):
        self.assertTrue(isinstance(self.new_source, NewsSourceModel))
