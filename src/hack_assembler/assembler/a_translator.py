import re


class ATranslator():
    def translate(self, instruction):
        if len(instruction) < 2:
            raise Exception("Invalid A-instruction")

        parse = instruction[1:]
        number = int(parse)

        if number > 24576:
            raise Exception("Out of bound memory")

        # convert number to 15-bit digit binary number
        number = f'{number:15b}'.replace(' ', '0')

        return '0' + number
