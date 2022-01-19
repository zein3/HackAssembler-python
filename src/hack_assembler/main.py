# Make a dictionary called variables that map labels and variables to their address
# Go through the file.asm line by line and copy only valid instruction and replace labels and variables with their corresponding number, output this file as file.o
# Use the CPU Emulator to test the output of file.o
# Convert file.o to file.hack, then delete file.o

from .assembler import Assembler
from .preprocessor import PreProcessor


class HackAssembler():
    def __init__(self):
        self.preprocessor = PreProcessor()
        self.assembler = Assembler()

    def assemble(self, filename: str) -> bool:
        """
        Assemble file with filename.asm into filename.hack
        Returns true for successful operation
        """
        try:
            with open(f'{filename}.asm', 'r') as file:
                code = self.preprocessor.preprocess(file)
                result = self.assembler.assemble(code)

                with open(f'{filename}.hack', 'w') as output:
                    for line in result:
                        output.write(line + '\n')
            return True
        except:
            return False

