%{

%}
Oct [0][0-9]+
Hex [0][x|X][0-9A-F]+

%%
{Hex} printf("This is Hexadecimal");
{Oct} printf("This is Octal");
%%

main()
{
	yylex();
}

int yywrap()
{
	return 1;
}


