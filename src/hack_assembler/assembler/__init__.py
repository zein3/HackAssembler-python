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
