import unittest
from my_awesome_lib import text_processing

class TestTextProcessing(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(text_processing.count_words("hello world"), 2)
        self.assertEqual(text_processing.count_words(""), 0)
        with self.assertRaises(TypeError):
            text_processing.count_words(None)

    def test_reverse_words(self):
        self.assertEqual(text_processing.reverse_words("hello world"), "world hello")
        self.assertEqual(text_processing.reverse_words(""), "")
        with self.assertRaises(TypeError):
            text_processing.reverse_words(12345)

    def test_remove_punctuation(self):
        self.assertEqual(text_processing.remove_punctuation("hello, world!"), "hello world")
        self.assertEqual(text_processing.remove_punctuation("no punctuation"), "no punctuation")
        with self.assertRaises(TypeError):
            text_processing.remove_punctuation(123)
