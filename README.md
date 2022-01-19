# Hack Assembler

## About
This program translates symbolic hack machine code into binary hack machine code that can be run by the computer made in the [Nand2Tetris](https://www.nand2tetris.org/) course.  

## Usage
On the command line:  
```bash
python3 -m hack_assembler filename # Assemble filename.asm into filename.hack
```

In python:
```python
from hack_assembler import HackAssembler
assembler = HackAssembler()
assembler.assemble("filename") # Assemble filename.asm into filename.hack
```
