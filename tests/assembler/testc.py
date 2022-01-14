from src.hack_assembler.assembler.c_translator import CTranslator
import unittest


class TestCTranslator(unittest.TestCase):
    def test_can_assign_to_dest(self):
        c_translator = CTranslator()

        result = c_translator.translate("M=D")
        self.assertEqual(result, "1110001100001000")

    def test_can_use_jump_condition(self):
        c_translator = CTranslator()

        result = c_translator.translate("D;JEQ")
        self.assertEqual(result, "1110001100000010")

    def test_can_translate_full_instruction(self):
        c_translator = CTranslator()

        result = c_translator.translate("AMD=D+1;JMP")
        self.assertEqual(result, "1110011111111111")


if __name__ == '__main__':
    unittest.main()
