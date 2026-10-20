# main.py
# Ryan McGough

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

# ========================================================================
# class FSM()
#
# Chose to define an FSM class as we will be reusing code from this later
# in the semester. Since we're using python, most of the code should be
# easily readable.
#
# FSM is stateful, and since it is defined as a class it will be an object.
# Make sure to reset the state of the FSM when appropriate if using helper
# functions defined within it. 
# ========================================================================
class FSM(): 

    # ========================================================================
    # States
    #
    # Transition will change the state of the class while working out the 
    # correct type for the string given each char. 
    # ========================================================================
    def __init__(self):
        self.state = "START"
    
    def reset(self):
        self.state = "START"

    def transition(self, char):
        if self.state == "START":
            if self.is_letter(char): 
                self.state = "Identifier"

            elif self.is_integer(char): 
                self.state = "Integer"

            elif char == ".":
                self.state = "DOT"

            else: 
                return False

        elif self.state == "Identifier": 
            if not (self.is_integer(char) 
                    or self.is_letter(char) 
                    or char  == "_"):
                return False
        
        elif self.state == "Integer":
            if self.is_integer(char): 
                pass
            elif char == ".":
                self.state = "INT_DOT"
            else:
                return False
            
        elif self.state in ("DOT", "INT_DOT"):
            if self.is_integer(char): 
                self.state = "Real"
            else:
                return False
            
        elif self.state == "Real":
            if not self.is_integer(char): 
                return False
            
        return True


    # ========================================================================
    # Character Helpers
    #
    # Wrapper classes for existing python functions. Added in the class for 
    # visibility sake, they don't expand on the library functions at all. 
    # ========================================================================
    def is_whitespace(self, char):
        return char.isspace()
    
    def is_letter(self, char):
        return char.isalpha()
    
    def is_integer(self, char):
        return char.isdigit()
      

    # ========================================================================
    # Skips
    #
    # Helper functions to skip massive blocks of text that don't do anything.
    # ========================================================================
    def skip_whitespaces(self, text, position):
        while position < len(text) and self.is_whitespace(text[position]):
            position += 1
        return position 
    
    def skip_comments(self, text, position):
        position += 1
        while position < len(text) and text[position] != "!":
            position += 1

        return position + 1
        

    # ========================================================================
    # run()
    #
    # Where the bread and butter of the FSM exists. This identifies the 
    # lexeme's type and sends it back to lexer(). 
    # ========================================================================
    def run(self, text, position):
        self.reset()
        start = position
        token_type = None


        # ========================================================================
        # Early escapes
        #
        # We don't need to enter the loop for identifying single character things.
        # This skips entering loops entirely, saving us time and troubleshooting. 
        # ========================================================================
        
        # Comments
        if text[position] == "!":
                position += 2

                # Catching "!=" before checking the rest of TWO_CHARACTER_OPERATORS
                # I have to build a case that checks if its a comment or the operator
                # anyway, so may as well build an early escape here. 
                if text[start:position] in TWO_CHARACTER_OPERATORS:
                    lexeme = text[start : position]
                    token_type = "Operator"

                    return token_type, lexeme, position
                
                else:
                    position = self.skip_comments(text, start)
                    lexeme = text[start:position]
                    token_type = "Comment"
                    
                    return token_type, lexeme, position
    

        elif text[position] in OPERATORS:
            if text[start : position + 2] in TWO_CHARACTER_OPERATORS:
                position += 2
                lexeme = text[start : position]
                token_type = "Operator"

                return token_type, lexeme, position
            
            else:
                position += 1
                lexeme = text[start]
                token_type = "Operator"

                return token_type, lexeme, position
            

        # "!" is not contained in SEPARATORS. 
        elif text[position] in SEPARATORS:
            position += 1
            lexeme = text[start]
            token_type = "Separator"

            return token_type, lexeme, position
        

        # Invalid character check. 
        # Remove this and it causes an infinite loop.
        elif not (
                self.is_letter(text[position]) 
                or self.is_integer(text[position])
                or text[position] == "."
                ):
            lexeme = text[start]
            position += 1
            token_type = "Unknown"
            return token_type, lexeme, position
        
        
        # None of the early escape conditions met. Time to enter the loop. 
        while position < len(text) and self.transition(text[position]):
            position += 1

        lexeme = text[start:position]
        if lexeme.lower() in KEYWORDS:
            token_type = "Keyword"
        
        elif self.state in {"Identifier", "Integer", "Real"}:
            token_type = self.state


        return token_type, lexeme, position


# =========================================================
# lexer()
#
# USES TWO RETURN TYPES. IF YOU CHANGE THIS,
# MAKE SURE TO ALWAYS RETURN POSITION AS THE SECOND TYPE
# OR THINGS WILL BREAK IN A REALLY ANNOYING WAY. 
# =========================================================
def lexer(source, position):
    fsm = FSM()

    position = fsm.skip_whitespaces(source, position)
    if position >= len(source):
        return None, position
    
    token_type, lexeme, position = fsm.run(source, position)

    return Token(token_type, lexeme), position

    

# =========================================================
# main()
#
# takes command line input, parses the file and sends text
# to the lexer for further analysis. will then print the 
# output into a .txt file in a very tidy table. 
#
# output file is compatible with markdown rendering for 
# quality of life. 
# =========================================================
def main():
    # Running this through the command line. 
    input_filename = ""
    output_filename = ""

    if len(sys.argv) > 1: 
        input_filename = sys.argv[1]

        if input_filename[-4:] != ".txt":
            print("ERROR: This program only works with .txt files. Please ensure that your file ends with '.txt'. \nExiting \n")
            sys.exit(1)

    else:
        print("Usage: python main.py <filename.txt>\n")
        sys.exit(1)
    

    try:
        output_filename = input_filename[:-4] + "_output.txt"
        position = 0


        with open(input_filename, "r") as f:
            source = f.read()

        tokens = []
        biggest = 0

        while True:
            token, position = lexer(source, position)
            if token is None:
                break

           # The assignment states to skip comments. We can easily change this later to include comments if need be. 
            if token.token == "Comment":
                continue 

            # Storing the biggest value from tokens and lexemes 
            # for formatting purposes in the output.
            if len(token.lexeme) > biggest:
                biggest = len(token.lexeme) + 1
            if len(token.token) > biggest:
                biggest = len(token.token) + 1

            tokens.append(token)


        with open(output_filename, "w") as out:
            token_spacing = " " * (biggest - 6)
            lexeme_spacing = " " * (biggest - 7)
            bar = "-" * biggest
            out.write(f"# {output_filename}"
                      f"\n\n"
                      f"| Token:{token_spacing} | Lexeme:{lexeme_spacing} |"
                      f"\n"
                      f"| {bar} | {bar} |"
                      f"\n"
                      )

            for t in tokens:
                token_spacing = " " * (biggest - len(t.token))
                lexeme_spacing = " " * (biggest - len(t.lexeme))
                out.write(
                    f"| {t.token}{token_spacing} | {t.lexeme}{lexeme_spacing} |"
                    f"\n"
                    )


        sys.exit(0)


    except FileNotFoundError:
        print(f"File not found: {input_filename} \nExiting\n")
        sys.exit(1)


# ===============================
# Entry Point (don't touch this!)
# ===============================
if __name__ == "__main__":
    main()


# References
# https://www.geeksforgeeks.org/c/c-lexical-analyser-lexer/
# https://www.geeksforgeeks.org/cpp/lexical-analyzer-in-cpp/