from flask import url_for
from flask_testing import TestCase

from service_2.app import app, occupation



class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_occupation(self):

        for _ in range(40):
            response = self.client.get(url_for('get_occupation'))

            self.assert200(response)
            self.assertIn(response.data.decode().replace('"','').strip(), occupation)
        