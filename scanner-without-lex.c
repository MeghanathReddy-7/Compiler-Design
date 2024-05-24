#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_TOKEN_LENGTH 100

int is_digit(char c) {
    return c >= '0' && c <= '9';
}

int is_letter(char c) {
    return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');
}

int is_delimiter(char c) {
    return c == '(' || c == ')' || c == '[' || c == ']' || c == '{' || c == '}' || c == ',';
}

int is_keyword(char *token) {
    char *keywords[] = {"auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern", "float", "for", "goto", "if", "int", "long", "register", "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"};
    int num_keywords = sizeof(keywords) / sizeof(keywords[0]);
    for (int i = 0; i < num_keywords; ++i) {
        if (strcmp(token, keywords[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

void tokenize(char *input) {
    char token[MAX_TOKEN_LENGTH];
    int i = 0, j = 0;

    while (input[i] != '\0') {
        if (isspace(input[i])) {
            i++;
            continue;
        }

        if (is_letter(input[i])) {
            token[j++] = input[i++];
            while (is_letter(input[i]) || is_digit(input[i])) {
                token[j++] = input[i++];
            }
            token[j] = '\0';
            if (is_keyword(token)) {
                printf("Keyword: %s\n", token);
            } else {
                printf("Identifier: %s\n", token);
            }
            j = 0;
        } else if (is_digit(input[i]) || (input[i] == '-' && is_digit(input[i + 1]))) {
            token[j++] = input[i++];
            while (is_digit(input[i]) || input[i] == '.') {
                token[j++] = input[i++];
            }
            token[j] = '\0';
            printf("Integer or Real: %s\n", token);
            j = 0;
        } else if (is_delimiter(input[i])) {
            token[j++] = input[i++];
            token[j] = '\0';
            printf("Delimiter: %s\n", token);
            j = 0;
        } else {
            printf("Special Symbol: %c\n", input[i++]);
        }
    }
}

int main() {
    char input[100];
    printf("Enter an expression: ");
    fgets(input, sizeof(input), stdin);
    tokenize(input);
    return 0;
}
