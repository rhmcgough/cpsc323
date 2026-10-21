# main.py - CPSC 323 Assignment 2: Syntax Analyzer (Recursive Descent Parser) for Rat26F

import sys
from lexer import lexer
 
PRINT_RULES = True                      # switch: print production rules or not
source = ""                             # whole input file
pos = 0                                 # where the lexer reads next
token_type = ""                         # current token type
lexeme = ""                             # current lexeme
line = 1                                # current line number
out = None                              # output file
