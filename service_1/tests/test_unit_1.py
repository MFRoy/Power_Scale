from flask import url_for
from flask_testing import TestCase
from requests_mock import mock

from service_1.application import app, db
from service_1.application.models import Powerscale

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db")
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()



class TestResponse(TestBase):

    def test_index(self):

        with mock() as m:
            m.get('http://service-2:5000/get/occupation', json='Sith Lord')
            m.get('http://service-3:5000/get/species', json='Jawa')
            m.post('http://service-4:5000/post/power', json=55)

            response = self.client.get(url_for('home'))

        self.assert200(response)
        self.assertIn('A Jawa Sith Lord has a power level of 55', response.data.decode())