from flask_script import Server,Manager
from app import create_app
from config import Config
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    # print(Config.API_KEY)
    # print(Config.BASE_URL)
    manager.run()