%{
#include <stdio.h>
#include <string.h>
%}

DIGIT       [0-9]
LETTER      [a-zA-Z]
IDENTIFIER  {LETTER}({LETTER}|{DIGIT})*
INTEGER     -?{DIGIT}+
REAL        -?{DIGIT}+"."{DIGIT}+
DELIMITER   [()[\]{},;]

%%
{INTEGER}       { printf("Integer: %s\n\n", yytext); }
{REAL}          { printf("Real: %s\n\n", yytext); }
{DELIMITER}     { printf("Delimiter: %s\n\n", yytext); }
{IDENTIFIER}    {
                    char *keywords[] = {"auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern", "float", "for", "goto", "if", "int", "long", "register", "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"};
                    int num_keywords = sizeof(keywords);
                    int i;
                    int is_keyword = 0;

                    for (i = 0; i < num_keywords; ++i) {
                        if (strcmp(yytext, keywords[i]) == 0) {
                            printf("Keyword: %s\n\n", yytext);
                            is_keyword = 1;
                            break;
                        }]

                    }

                    if (!is_keyword) {
                        printf("Identifier: %s\n\n", yytext);
                    }
                }
.               { printf("special symbol: %s\n\n", yytext); }

%%

int main() {
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}

