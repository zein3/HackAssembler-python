from src.hack_assembler.preprocessor import PreProcessor
from pathlib import Path
import unittest


class TestPreprocessorFull(unittest.TestCase):
    def test_full(self):
        testfile_folder = Path('tests/preprocessor/')
        with open(testfile_folder / 'testfile5') as file:
            with open(testfile_folder / 'testfile5.cmp') as compare_file:
                pp = PreProcessor()
                result = pp.main(file)
                cpp = PreProcessor()
                cpp.parse_file(compare_file)

                self.assertEqual(pp.code, cpp.code)


if __name__ == "__main__":
    unittest.main()
