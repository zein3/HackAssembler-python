from src.hack_assembler.assembler.a_translator import ATranslator
from pathlib import Path
import unittest


class TestATranslator(unittest.TestCase):
    def test_translation(self):
        a_translator = ATranslator()

        result = a_translator.translate('@123')
        self.assertEqual(result, '0000000001111011')

        result = a_translator.translate('@4121')
        self.assertEqual(result, '0001000000011001')

    def test_translation_error(self):
        a_translator = ATranslator()

        self.assertRaises(Exception, lambda: a_translator.translate('@'))


if __name__ == '__main__':
    unittest.main()
