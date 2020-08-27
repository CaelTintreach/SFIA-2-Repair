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

	def test_prediction(self):
		with patch('requests.get') as g:
			with patch('requests.post') as p:
				g.return_value.text = "A"
				p.return_value.text = "A"
				response = self.client.get(url_for('prediction'))
				self.assertIn(b'A', response.data)
				self.assertIn(b'A', response.data)
				self.assertEqual(response.status_code, 200)