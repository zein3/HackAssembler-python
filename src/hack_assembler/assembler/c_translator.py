from . import constants
import re


class CTranslator():
    def translate(self, instruction):
        parsed_instruction = self.parse(instruction)
        dest = self.dest_translate(parsed_instruction['dest'])
        comp = self.comp_translate(parsed_instruction['comp'])
        jump = self.jump_translate(parsed_instruction['jump'])

        return '111' + comp + dest + jump

    def parse(self, instruction: str) -> dict:
        if "=" in instruction and ";" in instruction:
            comp = re.search(r"(?<=\=).*(?=\;)", instruction)
        elif "=" in instruction:
            comp = re.search(r"(?<=\=).*", instruction)
        elif ";" in instruction:
            comp = re.search(r".*(?=\;)", instruction)
        else:
            comp = instruction

        if comp != None and type(comp) == re.Match:
            comp = comp[0]

        dest = re.search(r".*(?=\=)", instruction)
        if dest:
            dest = dest[0]

        jump = re.search(r"(?<=\;).*", instruction)
        if jump:
            jump = jump[0]

        return {
            'comp': comp,
            'dest': dest,
            'jump': jump
        }


    def comp_translate(self, comp: str or None) -> str:
        if not comp:
            return '0000000'

        try:
            result = constants.COMP_TABLE[comp]
        except:
            raise Exception('Invalid C-instruction (comp)')

        return result

    def dest_translate(self, dest: str or None) -> str:
        if not dest:
            return '000'

        d1 = '1' if 'A' in dest else '0'
        d2 = '1' if 'D' in dest else '0'
        d3 = '1' if 'M' in dest else '0'

        return d1 + d2 + d3

    def jump_translate(self, jump: str or None) -> str:
        if not jump:
            return '000'

        try:
            result = constants.JUMP_TABLE[jump]
        except:
            raise Exception("Invalid C-instruction (comp)")

        return result
