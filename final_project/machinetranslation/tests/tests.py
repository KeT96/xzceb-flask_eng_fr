import unittest

from translator import english_to_french
from translator import french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french('My name is'),'Mon nom est')
        self.assertNotEqual(english_to_french('Hello'),'Hallo')

    def test_french_to_english(self):
         self.assertEqual(french_to_english('Bonjour'),'Hello')
         self.assertEqual(french_to_english('Mon nom est'),'My name is')
         self.assertNotEqual(french_to_english('Bonjour'),'Ciao')

if __name__ == '__main__':
    unittest.main()