import unittest
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
	def create_app(self):
		return app

class TestView(TestBase):
	def test_randomname(self):
		response = self.client.get(url_for('user_name1'))
		self.assertEqual(response.status_code, 200)

class TestCountryName(TestBase):
	def test_countrynames(self):
		response = self.client.get(url_for('/prize/lgen'))
		check = False
		for item in ['A','B']:
			if bytes.decode(response.data) == item:
				check = True
		self.assertTrue(check)