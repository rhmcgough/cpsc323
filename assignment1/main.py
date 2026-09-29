import sys



KEYWORDS = {
    "integer",
    "boolean",
    "real",
    "if",
    "else",
    "fi",
    "while",
    "return",
    "get",
    "put",
    "function",
    "true",
    "false"
}
SEPARATORS = {
    "(",
    ")",
    "{",
    "}",
    ",",
    ";",
    "@",
}
OPERATORS = {
    "+",
    "-",
    "*",
    "/",
    "=",
    "<",
    ">",
}
TWO_CHARACTER_OPERATORS = {
    "!=",
    "==",
    "<=",
    ">="    
}


class Token: 
    def __init__(self, token, lexeme):
        self.token = token
        self.lexeme = lexeme 

class FSM:
    pass

def lexer():
    pass

    

# ==========================================
# main()
#
# parses the file and sends it to the lexer. 
# ==========================================
def main():
    global WRITE_COMMENTS
    # Running this through the command line. 
    input_filename = ""
    output_filename = ""

    if len(sys.argv) > 1: 
        input_filename = sys.argv[1]
    else:
        print("Usage: python main.py <filename.txt>\n")
        sys.exit(1)
    

    try:
        output_filename = input_filename[:-4] + "_output.txt"
        position = 0

        
        with open(input_filename, "r") as f:
            source = f.read()

        tokens = []

        while True:
            token, position = lexer(source, position)
            if token is None:
                break

            if not WRITE_COMMENTS:
                if token.token == "Comment":
                    continue 

            tokens.append(token)
        
        with open(output_filename, "w") as out:

            # Writing in markdown format.
            out.write(f"# {output_filename}\n\n"
                      f"| Token | Lexeme |\n", 
                      f"| ----- | ------ | \n"
            )
            for t in tokens:
                out.write(f"| {t.token} | {t.lexeme} |\n")

        sys.exit(0)


    except FileNotFoundError:
        print(f"File not found: {input_filename} \nExiting Program")
        sys.exit(1)


# ===============================
# Entry Point (don't touch this!)
# ===============================
if __name__ == "__main__":
    main()


# References
# https://www.geeksforgeeks.org/c/c-lexical-analyser-lexer/
# https://www.geeksforgeeks.org/cpp/lexical-analyzer-in-cpp/
