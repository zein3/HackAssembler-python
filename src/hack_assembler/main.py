# Make a dictionary called variables that map labels and variables to their address
# Go through the file.asm line by line and copy only valid instruction and replace labels and variables with their corresponding number, output this file as file.o
# Use the CPU Emulator to test the output of file.o
# Convert file.o to file.hack, then delete file.o

from . import assembler
from .preprocessor import PreProcessor
import sys
import re


def main():
    if len(sys.argv) < 2:
        print("file name not found")
        return

    full_file_name = sys.argv[1]
    file_name = re.search(r".*(?=\.)", full_file_name)
    if file_name != None and type(file_name) == re.Match:
        file_name = file_name[0]
    else:
        file_name = full_file_name

    with open(full_file_name, 'r') as file:
        pp = PreProcessor()

        result = pp.preprocess(file)
        result = assembler.assemble(result)

        with open(file_name + '.hack', 'w') as output:
            for line in result:
                output.write(line + '\n')
