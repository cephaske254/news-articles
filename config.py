import os


class Config:
    BASE_URL = 'https://newsapi.org/v2/{}?apiKey={}&{}'
    API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    DEBUG = False


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
