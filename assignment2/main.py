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


# True if current token is this type (Identifier...) or this lexeme (if, ;, +...)
def is_(x):
    return token_type == x or lexeme.lower() == x


# Check the current token, then move to the next one
def match(x):
    if is_(x):
        next_token()
    else:
        error("'" + x + "'")

# True if current token is integer / boolean / real
def is_qualifier():
    return is_("integer") or is_("boolean") or is_("real")


# True if current token can start a statement
def is_statement():
    return is_("Identifier") or is_("{") or is_("if") or is_("return") or is_("put") or is_("get") or is_("while")

# R1. <Rat26F> -> <Opt Function Definitions> @ <Opt Declaration List> @ <Statement List>
def rat26f():
    rule("<Rat26F> -> <Opt Function Definitions> @ <Opt Declaration List> @ <Statement List>")
    while is_("function"):
        function_def()
    match("@")
    declaration_list()
    match("@")
    statement_list()
    if token_type != "EOF":
        error("end of file")


# R4. <Function> -> function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>
def function_def():
    rule("<Function> -> function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>")
    match("function")
    match("Identifier")
    match("(")
    if is_("Identifier"):
        parameter()
        while is_(","):
            match(",")
            parameter()
    match(")")
    declaration_list()
    rule("<Body> -> { <Statement List> }")
    match("{")
    statement_list()
    match("}")

# R7. <Parameter> -> <IDs> <Qualifier>
def parameter():
    rule("<Parameter> -> <IDs> <Qualifier>")
    ids()
    qualifier()
 
# R8. <Qualifier> -> integer | boolean | real
def qualifier():
    if not is_qualifier():
        error("integer, boolean or real")
    rule("<Qualifier> -> " + lexeme.lower())
    next_token()


# R10-R12. <Opt Declaration List>: zero or more "<Qualifier> <IDs> ;"
def declaration_list():
    if not is_qualifier():
        rule("<Opt Declaration List> -> <Empty>")
    while is_qualifier():
        rule("<Declaration> -> <Qualifier> <IDs>")
        qualifier()
        ids()
        match(";")
 
# R13. <IDs> -> <Identifier> <IDs Prime>,  <IDs Prime> -> , <IDs> | <Empty>
def ids():
    rule("<IDs> -> <Identifier> <IDs Prime>")
    match("Identifier")
    while is_(","):
        rule("<IDs Prime> -> , <IDs>")
        match(",")
        match("Identifier")
    rule("<IDs Prime> -> <Empty>")


# R14. <Statement List> -> <Statement> <Statement List Prime>
def statement_list():
    rule("<Statement List> -> <Statement> <Statement List Prime>")
    statement()
    while is_statement():
        statement()
    rule("<Statement List Prime> -> <Empty>")


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
