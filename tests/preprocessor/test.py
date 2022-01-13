from src.hack_assembler import preprocessor
from pathlib import Path
import unittest


class TestPreprocessor(unittest.TestCase):
    def setUp(self):
        testfile_folder = Path('tests/preprocessor/')
        self.file1 = open(testfile_folder / "testfile1")
        self.file2 = open(testfile_folder / "testfile2")
        self.file3 = open(testfile_folder / "testfile3")

        self.code3 = preprocessor.parse_file(self.file3)

    def test_can_parse_file(self):
        result = preprocessor.parse_file(self.file1)
        self.assertEqual(result, ['Testing', 'Second Line', 'Third Line'])

    def test_can_parse_file_without_EOF(self):
        result = preprocessor.parse_file(self.file2)
        self.assertEqual(result, ['test1', 'test2'])

    def test_can_clean_code(self):
        result = preprocessor.clean_code(self.code3)

        self.assertEqual(result, ['@12', '(TEST)', 'A=D', '@TEST', 'D;JGT', '(END)', '@END', '0;JMP'])

    def test_can_find_all_label_declarations(self):
        initial_length = len(preprocessor.variables)
        result = preprocessor.find_labels(preprocessor.clean_code(self.code3))
        final_length = len(preprocessor.variables)

        self.assertEqual(result, ['@12', 'A=D', '@TEST', 'D;JGT', '@END', '0;JMP'])
        self.assertTrue((final_length - initial_length) == 2)
        self.assertTrue("TEST" in preprocessor.variables and "END" in preprocessor.variables)
        self.assertTrue(preprocessor.variables["TEST"] == 1 and preprocessor.variables["END"] == 4)

    # def test_can_replace_symbols(self):
        # pass

    # def test_full_testing_1(self):
        # pass

    # def test_full_testing_2(self):
        # pass

    def tearDown(self):
        self.file1.close()
        self.file2.close()
        self.file3.close()


if __name__ == '__main__':
    unittest.main()
