from flask import url_for
from flask_testing import TestCase
from requests_mock import mock

from service_1.app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_index(self):

        with mock() as m:
            m.get('http://service-2:5000/get/species', text='Jawa')
            m.get('http://service-3:5000/get/occupation', text='Sith Lord')
            m.post('http://service-4:5000/post/power', json=55)

            response = self.client.get(url_for('index'))

        self.assert200(response)
        self.assertIn('A Jawa Sith Lord has a power level of 55', response.data.decode())