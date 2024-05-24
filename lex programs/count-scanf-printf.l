%{
#include<stdio.h>
#include<string.h>
int s=0,p=0;
%}

SCANF scanf
PRINTF printf

%%
{SCANF} {s+=1;}
{PRINTF} {p+=1;}
.      ;
%%

int main(){
  yylex();
  printf("Scanf count = %d, Printf count = %d\n", s,p);
  return 0;
}

int yywrap(){
  return 1;
}
