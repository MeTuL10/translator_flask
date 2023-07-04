import unittest
from machinetranslation import translator

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(translator.english_to_french("Hello"),"Bonjour")
        self.assertNotEqual(translator.english_to_french("bye"),"Bonjour")
    def test_french_to_english(self):
        self.assertEqual(translator.french_to_english("Bonjour"),"Hello")
        self.assertNotEqual(translator.french_to_english("Bonjour"),"bye")

if __name__=="__main__":
    unittest.main()
