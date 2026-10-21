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









# Read the file, parse it, write the output file
def main():
    global source, out
    if len(sys.argv) < 2 or sys.argv[1][-4:] != ".txt":
        print("Usage: python main.py <filename.txt>")
        return
    try:
        source = open(sys.argv[1]).read()
    except FileNotFoundError:
        print("File not found: " + sys.argv[1])
        return
 
    out_name = sys.argv[1][:-4] + "_output.txt"
    out = open(out_name, "w")
    next_token()
    rat26f()
    out.write("\nParsing finished: no syntax errors.\n")
    out.close()
    print("No syntax errors. Output written to " + out_name)
 
 
main()
