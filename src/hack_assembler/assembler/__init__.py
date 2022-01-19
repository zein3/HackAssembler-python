# If instruction starts with @n where n is an integer, it's an A-instruction,
# the resulting machine code will be: '0' + binary(n).
# otherwise it is a C-instruction, therefore it must be parsed into three components:
# - comp
# - dest
# - jump
# and the resulting machine code will be '111' + comp + dest + jump

from .assembler import Assembler
