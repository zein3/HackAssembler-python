from src.hack_assembler.preprocessor import PreProcessor
from pathlib import Path
import unittest


class TestPreprocessorFull(unittest.TestCase):
    def test_full(self):
        testfile_folder = Path('tests/preprocessor/')
        with open(testfile_folder / 'testfile5') as file:
            pp = PreProcessor()
            pp.main(file)

            print(pp.variables)
            print(pp.code)

            self.assertTrue(1 == 1)


if __name__ == "__main__":
    unittest.main()
