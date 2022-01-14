# If instruction starts with @n where n is an integer, it's an A-instruction,
# the resulting machine code will be: '0' + binary(n).
# otherwise it is a C-instruction, therefore it must be parsed into three components:
# - comp
# - dest
# - jump
# and the resulting machine code will be '111' + comp + dest + jump

from . import a_translator
from . import c_translator


def assemble(symbolic_code: list) -> list:
    atranslator = a_translator.ATranslator()
    ctranslator = c_translator.CTranslator()

    machine_code = []
    for line in symbolic_code:
        if line.startswith("@"):
            instruction = atranslator.translate(line)
        else:
            instruction = ctranslator.translate(line)
        machine_code.append(instruction)

    return machine_code
