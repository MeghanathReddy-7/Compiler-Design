%{
#include <stdio.h>
%}

DIGIT -?[0-9]
INTEGER -?[0-9]+
REAL -?[0-9]+\.[0-9]+

%%

{INTEGER} {printf("Integer : %s",yytext);}
{REAL} {printf("Real : %s", yytext);}

%%

main(){
  yylex();
}

int yywrap()
{
  return 1;
}

