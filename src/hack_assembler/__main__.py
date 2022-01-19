from .main import HackAssembler

import sys


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: hack_assembler <filename>")
        sys.exit()

    hack_assembler = HackAssembler()
    hack_assembler.assemble(sys.argv[1])
