#!/usr/bin/env bash

#python -m unittest discover -s 'tests'
python -m tests.preprocessor.test
python -m tests.preprocessor.testfull
python -m tests.assembler.testa
python -m tests.assembler.testc
