import unittest
from machinetranslation.translator import englishToFrench, frenchToEnglish


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("hello"), "bonjour")

    def test2(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")


unittest.main()
