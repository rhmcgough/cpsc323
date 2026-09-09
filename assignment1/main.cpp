// Ryan McGough

// Don't touch these. Add if you need, but don't remove any. 
#include <iostream>
#include <string> 
#include <unordered_map>
#include <vector>
#include <fstream>

/* 

struct TOKEN {
    TOKEN_TYPE type;
    std::string value;

    TOKEN(TOKEN_TYPE t, const std::string& v)
        : type(t)
        , value(v)
        {}
};


enum class TOKEN_TYPE {
    IDENTIFIER,
    INT,
    REAL,
    KEYWORD,
    OPERATOR,
    SEPARATOR,
    END_OF_FILE,
    UNKNOWN
};  


/**========================================================================================*
*
* Lexeme Library
* 
* Storing all possible lexemes here, anything else should send unknown or a compiler error.
*
*==========================================================================================*/
const std::unordered_map <std::string, bool> keywords = 
{
    {"integer", true},
    {"boolean", true},
    {"real", true},
    {"if", true},
    {"else", true},
    {"fi", true},
    {"while", true},
    {"return", true},
    {"get", true},
    {"put", true},
    {"function", true},
    {"true", true},
    {"false", true}
};

// Map of separators
const std::unordered_map <std::string, bool> separators = 
{
    {"(", true},
    {")", true},
    {";", true},
    {":", true}
};


// Map of operators
const std::unordered_map <std::string, bool> operators = 
{
    {"<", true},
    {">", true},
    {"+", true},
    {"-", true},
    {"/", true},
    {"*", true},
    {"|", true},
    {"&", true},
    {"!", true},
    {"^", true},
};


// string getTokenType (TOKEN_TYPE)
//
// helper function for quick finding a token type. Call this someplace in the lexer.
/*
std::string getTokenType (std::string& testToken)
{
    switch (type) {
        case lexer.isNum(c):
            return "IDENTI";

        case TOKEN_TYPE::INT:
            return "INT";

        case TOKEN_TYPE::REAL:
            return  "REAL";

        case TOKEN_TYPE::KEYWORD:
            return "KEYWORD";

        case TOKEN_TYPE::OPERATOR:
            return "OPERATOR";

        case TOKEN_TYPE::SEPARATOR:
            return "SEPARATOR";

        case TOKEN_TYPE::END_OF_FILE:
            return "END_OF_FILE";
    }
    return "UNKNOWN";
}
*/



// TODO: Update this so that it parses the test files.
class lexer {
    private:
        size_t position = 0;
        int line = 1;

        char peek();
        char advance();
        void skip();
        TOKEN scanKeyword();
        TOKEN scanNumber();
        TOKEN scanOperatorSeparator();

        // No point making a map for these two. 
        bool isNum(char c) { return (c >= '0' && c <= '9'); }
        bool isLetter(char c) { return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'); }


        bool isKeyword(std::string& key) { return keywords.find(key) != keywords.end(); }


        bool isSeparator(const char c)
        {
            std::string key;
            key += c;
            if (separators.find(key) == separators.end()) 
            { return false; }
            else return true;
        }

        bool isOperator(std::string& key) { return operators.find(key) != operators.end(); }

        bool isUnknown(const char c)
        {
            // basically call all the other functions here, if none of them work then return this. 
            return true;
        }
        /*
        IDENTIFIER,
        REAL,
        KEYWORD,
        END_OF_FILE,
        */




    public:
        lexer(const std::string& src);
        TOKEN getNextToken();
};


void writeTokens(std::ostream& fout)
{
    
}

// runLexer
// Create a string tokenTest to store chars. When there is a whitespace reached, send it to another helper function
// to determine what kind of token it is, or send a compiler error. 
void runLexer(std::ifstream& fin, std::ostream& fout)
{
    char c;
    std::string tokenString = "";

    while(fin.get(c))
    {
        tokenString += c;
    }
}

*/

// Keep this tidy
// I want to create a separate helper function for reading the file, that way all the test files can be read in one execution. 
int main() {

    // Open an input and output file
    std::ifstream inputFile("sample.txt", std::fstream::in);
    std::ofstream outputFile("sample2.txt", std::fstream::out);


    // Error handling
    if (!inputFile.is_open() && outputFile.is_open())
    {
        std::cout << "Error opening file. Closing program\n";
        return 0;
    }
    else
    {
        runLexer(inputFile, outputFile);
    }


    // Close the files and end the program. 
    inputFile.close();
    outputFile.close();
    std::cout << "File completed parsing, closing program...\n";
    return 0;
}