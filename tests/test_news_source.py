import unittest
from app.models import NewsSourceModel,NewsArticleModel

class TestNewsSource(unittest.TestCase):
    def setUp(self):
        '''
        Setup method that will be run before every test
        '''
        self.new_source = NewsSourceModel(1,'techNews')

    def test_init(self):
        self.assertTrue(isinstance(self.new_source, NewsSourceModel))


class TestNewsArticleModel(unittest.TestCase):
    def SetUp(self):
    '''
    '''
    pass