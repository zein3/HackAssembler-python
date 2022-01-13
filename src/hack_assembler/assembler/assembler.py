# If instruction starts with @n where n is an integer, it's an A-instruction,
# the resulting machine code will be: '0' + binary(n).
# otherwise it is a C-instruction, therefore it must be parsed into three components:
# - comp
# - dest
# - jump
# and the resulting machine code will be '111' + comp + dest + jump

from src.hack_assembler.assembler.a_translator import ATranslator
from src.hack_assembler.assembler.c_translator import CTranslator


class Assembler():
    def __init__(self):
        self.a_translator = ATranslator()
        self.c_translator = CTranslator()

    def main(self, symbolic_code):
        machine_code = []
        for line in symbolic_code:
            if line.startswith("@"):
                instruction = self.a_translator.translate(line)
            else:
                instruction = self.c_translator.translate(line)
            machine_code.append(instruction)

        #TODO
