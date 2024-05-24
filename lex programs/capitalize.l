%{
#include <stdio.h>
#include <ctype.h>

void capitalize(char * str)
{
    int i;
    for (i = 0; str[i]; i++) {
        str[i] = toupper(str[i]);
    }
    printf("%s",str);
}

void func(char *  str){
	str[0]=toupper(str[0]);
	printf("%s",str);
}

%}

STRING [a-zA-Z]+


%%
. {func(yytext);}
%%


main()
{
	yylex();
}

int yywrap()
{
	return 1;
}

