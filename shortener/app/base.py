# services/users/project/tests/base.py


from flask_testing import TestCase

from app import db
from app import create_app

current_app = create_app()


class BaseConfig:
    """Base configuration"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'something_secret'


class BaseTestCase(TestCase):
    def create_app(self):
        current_app.config.from_object('project.config.TestingConfig')
        return current_app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
