# Replace labels and variables with their corresponding addresses (only A instruction contains labels or variables).
# Remove blank lines and comments (both line and in-line).
# The output file.o should be identical to the binary loaded to the CPU Emulator.

import re
from . import utils

INITIAL_VARIABLES = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "SCREEN": 16384,
    "KBD": 24576,
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4
}


class PreProcessor():
    def __init__(self):
        self.variables = INITIAL_VARIABLES

    def preprocess(self, file) -> list:
        self.parse_file(file)
        self.clean_code()
        self.find_labels()
        self.replace_symbols()

        return self.code

    def parse_file(self, file):
        """
        Parse the file into an array of strings
        """
        result = file.read().split("\n")
        if (result[len(result) - 1]):
            self.code = result
        else:
            self.code = result[0:len(result) - 1]

    def clean_code(self):
        """
        Remove all blank lines and comments from the file, as well as trim every instruction.
        Don't delete labels as they're going to be used later.
        """
        if not self.code:
            return

        cleanedCode = []
        for line in self.code:
            # Remove blank lines and line comments
            if line == '' or line.startswith('//'):
                continue

            # Remove inline comments
            line = re.sub(r"\/\/.*", "", line)

            # Delete all whitespace
            line = re.sub(r"\s", "", line)

            cleanedCode.append(line)

        self.code = cleanedCode

    def find_labels(self):
        """
        Find all label declarations in code to add them to variables dictionary and then remove them from the code.
        """
        if not self.code:
            return

        result = []
        i = 0
        for line in self.code:
            labels = re.search(r"(?<=\()(.+)(?=\))", line)
            if labels:
                self.variables[labels[0]] = i
            else:
                result.append(line)
                i += 1

        self.code = result

    def replace_symbols(self):
        """
        Replace all the symbols in the code with addresses (all symbols are in A-instruction).
        When an unknown symbol is found, allocate it to an unused address.
        """
        if not self.code:
            return

        result = []
        for line in self.code:
            if re.search(r"^@[^0-9]+", line):
                # get the variable name
                var = re.search(r"(?<=@).+", line)
                if not var:
                    raise Exception(f"Invalid A-instruction: {line}")
                var = var[0]

                # if var doesn't exist, allocate a memory to it
                if var not in self.variables:
                    utils.allocate_memory(self.variables, var)

                # make the instruction
                instruction = f"@{self.variables[var]}"
            else:
                instruction = line

            result.append(instruction)

        self.code = result
