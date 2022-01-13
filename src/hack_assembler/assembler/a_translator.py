import re


class ATranslator():
    def translate(self, instruction):
        parse = re.search(r"(?<=@)[0-9]+", instruction)
        if not parse:
            raise Exception("Invalid A-instruction")

        number = int(parse[0])

        if number > 24576:
            raise Exception("Out of bound memory")

        # convert number to 15-bit digit binary number
        number = f'{number:15b}'.replace(' ', '0')

        return '0' + number
