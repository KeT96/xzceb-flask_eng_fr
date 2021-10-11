import unittest

from translator import englishToFrench
from translator import frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertEqual(englishToFrench('My name is'),'Mon nom est')
        

    def test_frenchToEnglish(self):
         self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
         self.assertEqual(frenchToEnglish('Mon nom est'),'My name is')

if __name__ == '__main__':
    unittest.main()