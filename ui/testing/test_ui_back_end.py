import unittest
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
	def create_app(self):
		return app

class TestUI(TestBase):
	def test_home(self):
		response = self.client.get(url_for('home'))
		self.assertEqual(response.status_code, 200)