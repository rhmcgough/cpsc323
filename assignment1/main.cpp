// Ryan McGough


#include <iostream>
#include <string> 
#include <unordered_map>
#include <vector>


enum class TOKEN_TYPE {
    IDENTIFIER,
    INT,
    REAL,
    KEYWORD,
    OPERATOR,
    SEPARATOR,
    COMMENT,
    WHITESPACE
};  


struct TOKEN {
    TOKEN_TYPE type;
    std::string value;

    TOKEN(TOKEN_TYPE t, const std::string& v)
        : type(t)
        , value(v)
        {}
};



// string getTokenType (TOKEN_TYPE)
//
// helper function for quick finding a token type. Call this someplace in the lexer.

std::string getTokenType (TOKEN_TYPE type)
{
    switch (type) {
        case TOKEN_TYPE::IDENTIFIER:
            return "IDENTIFIER";
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
        case TOKEN_TYPE::COMMENT:
            return "COMMENT";
        case TOKEN_TYPE::WHITESPACE:
            return "WHITESPACE";
    }
}


// TODO: Update this so that it parses the test files.
class lexer {
    public: 
    private:
};


// Keep this tidy
// I want to create a separate helper function for reading the file, that way all the test files can be read in one execution. 
int main() {

    return 0;
}