from src.hack_assembler.preprocessor import PreProcessor
from pathlib import Path
import unittest


class TestPreprocessor(unittest.TestCase):
    def setUp(self):
        testfile_folder = Path('tests/preprocessor/')
        self.file1 = open(testfile_folder / "testfile1")
        self.file2 = open(testfile_folder / "testfile2")
        self.file3 = open(testfile_folder / "testfile3")
        self.file4 = open(testfile_folder / "testfile4")
        self.file5 = open(testfile_folder / "testfile5")
        self.file5cmp = open(testfile_folder / "testfile5.cmp")

    def test_can_parse_file(self):
        pp = PreProcessor()
        pp.parse_file(self.file1)
        self.assertEqual(pp.code, ['Testing', 'Second Line', 'Third Line'])


    def test_can_parse_file_without_EOF(self):
        pp = PreProcessor()
        pp.parse_file(self.file2)
        self.assertEqual(pp.code, ['test1', 'test2'])

    def test_can_clean_code(self):
        pp = PreProcessor()
        pp.parse_file(self.file3)
        pp.clean_code()

        self.assertEqual(pp.code, ['@12', '(TEST)', 'A=D', '@TEST', 'D;JGT', '(END)', '@END', '0;JMP'])

    def test_can_find_all_label_declarations(self):
        pp = PreProcessor()

        initial_length = len(pp.variables)
        pp.parse_file(self.file3)
        pp.clean_code()
        pp.find_labels()
        final_length = len(pp.variables)

        self.assertEqual(pp.code, ['@12', 'A=D', '@TEST', 'D;JGT', '@END', '0;JMP'])
        self.assertTrue((final_length - initial_length) == 2)
        self.assertTrue("TEST" in pp.variables and "END" in pp.variables)
        self.assertTrue(pp.variables["TEST"] == 1 and pp.variables["END"] == 4)

    def test_can_replace_labels(self):
        pp = PreProcessor()
        pp.parse_file(self.file3)
        pp.clean_code()
        pp.find_labels()
        pp.replace_symbols()

        self.assertEqual(pp.code, ['@12', 'A=D', '@1', 'D;JGT', '@4', '0;JMP'])

    def test_can_allocate_variables(self):
        pp = PreProcessor()
        pp.parse_file(self.file4)
        pp.replace_symbols()

        self.assertEqual(pp.code, ['@16', 'M=1', '@17', 'M=0'])

    # def test_full(self):
        # result = preprocessor.preprocessor(self.file5)
        # compare = preprocessor.parse_file(self.file5cmp)
        # print(result)

        # self.assertEqual(result, compare)

    def tearDown(self):
        self.file1.close()
        self.file2.close()
        self.file3.close()
        self.file4.close()
        self.file5.close()
        self.file5cmp.close()


if __name__ == '__main__':
    unittest.main()
