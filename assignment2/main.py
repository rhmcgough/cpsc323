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


# Print a production rule if the switch is on
def rule(text):
    if PRINT_RULES:
        out.write("     " + text + "\n")

# Get the next token (skip comments) and print it
def next_token():
    global pos, token_type, lexeme, line
    tok, pos = lexer(source, pos)
    while tok is not None and tok.token == "Comment":
        tok, pos = lexer(source, pos)
    if tok is None:
        token_type = "EOF"
        lexeme = "EOF"
        return
    token_type = tok.token
    lexeme = tok.lexeme
    line = tok.line
    out.write("Token: " + token_type.ljust(12) + "Lexeme: " + lexeme + "\n")


# Print an error message and stop
def error(expected):
    msg = "Error at line " + str(line) + ": expected " + expected + " but found " + token_type + " '" + lexeme + "'"
    out.write("\n" + msg + "\n")
    out.close()
    print(msg)
    sys.exit(1)
