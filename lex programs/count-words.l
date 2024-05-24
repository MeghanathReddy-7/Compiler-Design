%{
int word_count = 1;
%}

%%

[\t\n  ]    { word_count++; }
.            ;

%%

int main() {
    yylex();
    printf("\nNumber of words: %d\n", word_count);
    return 0;
}

int yywrap() {
    return 1;
}

