import unittest
from flask import Flask
from flask.testing import FlaskClient
from deep_translator import MyMemoryTranslator
from translator import app, english_to_french, french_to_english

class TranslationTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_english_to_french(self):
        response = self.client.get('/englishToFrench?textToTranslate=Hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Translated text to French: Bonjour')

    def test_french_to_english(self):
        response = self.client.get('/frenchToEnglish?textToTranslate=Bonjour')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Translated text to English: Hello')

if __name__ == '__main__':
    unittest.main()
