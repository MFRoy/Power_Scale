from flask import url_for
from flask_testing import TestCase

from app import app, power

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_occupation(self):

        for occupation in power['occupation']:
            for species in power['species']:

                powers = {'occupation':occupation, 'species':species}
                response = self.client.post(url_for('post_power'), json=powers)

                self.assert200(response)

                expected_power = ((power['occupation'][occupation] + power['species'][species]))
                self.assertEqual(response.json, expected_power)
        