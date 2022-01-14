import re


class ATranslator():
    def translate(self, instruction):
        if len(instruction) < 2:
            raise Exception("Invalid A-instruction")

        parse = instruction[1:]
        number = int(parse)

        # convert number to 15-bit digit binary number
        number = f'{number:15b}'.replace(' ', '0')

        return '0' + number
