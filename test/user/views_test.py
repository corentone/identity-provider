import unittest
import urlparse

import requests

import flask.ext.testing
import app as app_module


class TestSequenceFunctions(flask.ext.testing.LiveServerTestCase):
    @staticmethod
    def create_app():
        app = app_module.create_app()
        app.config['TESTING'] = True
        # Default port is 5000
        app.config['LIVESERVER_PORT'] = 8943
        return app

    def url(self, url):
        return urlparse.urljoin(self.get_server_url(), url)

    def test_get_users(self):
        response = requests.get(self.url('/users'))
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()