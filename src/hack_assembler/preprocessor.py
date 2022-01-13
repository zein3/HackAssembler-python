# Replace labels and variables with their corresponding addresses (only A instruction contains labels or variables).
# Remove blank lines and comments (both line and in-line).
# The output file.o should be identical to the binary loaded to the CPU Emulator.

import re


variables = {
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


def preprocessor(file):
    code = parse_file(file)
    clean_code(code)
    find_labels(code)
    replace_symbols(code)


def parse_file(file):
    """
    Parse the file into an array of strings
    """
    result = file.read().split("\n")
    if (result[len(result) - 1]):
        return result
    else:
        return result[0:len(result) - 1]


def clean_code(code):
    """
    Remove all blank lines and comments from the file, as well as trim every instruction.
    Don't delete labels as they're going to be used later.
    """
    cleanedCode = []
    for line in code:
        # Remove blank lines and line comments
        if line == '' or line.startswith('//'):
            continue

        # Remove inline comments
        line = re.sub(r"\/\/.*", "", line)

        # Delete all whitespace
        line = re.sub(r"\s", "", line)

        cleanedCode.append(line)

    return cleanedCode


def find_labels(code):
    """
    Find all label declarations in code to add them to variables dictionary and then remove them from the code.
    """
    pass


def replace_symbols(code):
    """
    Replace all the symbols in the code with addresses (all symbols are in A-instruction).
    When an unknown symbol is found, allocate it to an unused address.
    """
    pass
