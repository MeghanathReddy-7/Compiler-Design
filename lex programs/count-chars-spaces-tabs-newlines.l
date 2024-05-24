%{
#include<stdio.h>
int lc=0,sc=0,tc=0,cc=0;
%}

SPACE [ ]
TAB [\t]
LINE [\n]

%%

{SPACE} {sc++;cc+=1;}
{LINE} {lc++;cc+=1;}
{TAB} {tc++;cc+=4;}
. {cc++;}

%%

int main(){
  FILE* file;
  file = fopen("hello.txt","r");
  if(file==NULL){
    printf("No file");
    return 0;
  }
  yyin=file;
  yylex();
  printf("Characters, spaces, lines, tabs = %d,%d,%d,%d",cc,sc,lc,tc);
  return 0;
}

int yywrap(){
  return 1;
}


