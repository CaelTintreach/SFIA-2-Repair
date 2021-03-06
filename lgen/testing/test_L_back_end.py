import unittest
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
	def create_app(self):
		return app

class TestView(TestBase):
	def test_gview(self):
		response = self.client.get(url_for('lGen'))
		self.assertEqual(response.status_code, 200)

class TestGen(TestBase):
	def test_gen(self):
		response = self.client.get(url_for('lGen'))
		check = False
		for item in ['A','B']:
			if bytes.decode(response.data) == item:
				check = True
		self.assertTrue(check)