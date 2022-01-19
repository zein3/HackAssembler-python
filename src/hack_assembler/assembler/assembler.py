from .a_translator import ATranslator
from .c_translator import CTranslator


class Assembler():
    def __init__(self):
        self.a_translator = ATranslator()
        self.c_translator = CTranslator()

    def assemble(self, symbolic_code: list) -> list:
        machine_code = []
        for line in symbolic_code:
            if line.startswith("@"):
                instruction = self.a_translator.translate(line)
            else:
                instruction = self.c_translator.translate(line)
            machine_code.append(instruction)

        return machine_code
