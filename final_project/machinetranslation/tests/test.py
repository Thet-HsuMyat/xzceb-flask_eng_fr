import unittest
from translator import english_to_french
from translator import french_to_english

class TestMyModule(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('None'),'')

class TestMyModuleFrToEng(unittest.TestCase):
    def test_french_to_english(self):
        self.assertNotEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('None'),'')

unittest.main()