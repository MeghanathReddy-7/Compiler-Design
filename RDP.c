#include <stdio.h>
#include <string.h>
 
#define SUCCESS 1
#define FAILED 0


//defining functions
int E(), Edash(), T(), Tdash(), F();


char *cursor;
char string[64];

char* match(char *c){
    c++;
    return c;
}

int main(){
    puts("Enter the string");
    scanf("%s", string);
    cursor = string;
    puts("");
    puts("Input          Action");
    puts("--------------------------------");

    if (E() && *cursor == '\0') { 
        puts("--------------------------------");
        puts("String is successfully parsed");
        return 0;
    } 
    else {
        puts("--------------------------------");
        puts("Error in parsing String");
        return 1;
    }

    return 0;
}

int E(){
    printf("%-16c E -> T E'\n", *cursor);
    if(T()){
        if(Edash()){
            return SUCCESS;
        }
        else{
            return FAILED;
        }
    }
    else{
        return FAILED;
    }
}

int Edash(){
    if(*cursor == '+'){
        printf("%-16c E' -> + T E'\n", *cursor);
        cursor = match(cursor);
        if (T()) {
            if (Edash())
                return SUCCESS;
            else
                return FAILED;
        } 
        else
            return FAILED;
    }
    else{
        printf("%-16c E' ->  $\n", *cursor);
        return SUCCESS;
    }
}

int T(){
    printf("%-16c T -> F T'\n", *cursor);
    if(F()){
        if(Tdash()){
            return SUCCESS;
        }
        else{
            return FAILED;
        }
    }
    else{
        return FAILED;
    }
}

int Tdash() {
    if (*cursor == '*') {
        printf("%-16c T' -> * F T'\n", *cursor);
        cursor = match(cursor);
        if (F()) {
            if (Tdash())
                return SUCCESS;
            else
                return FAILED;
        } 
        else
            return FAILED;
    } 
    else {
        printf("%-16c T' -> $\n", *cursor);
        return SUCCESS;
    }
}

int F() {
    if (*cursor == '(') {
        printf("%-16c F -> ( E )\n", *cursor);
        cursor = match(cursor);
        if (E()) {
            if (*cursor == ')') {
                cursor = match(cursor);
                return SUCCESS;
            } 
            else
                return FAILED;
        } 
        else
            return FAILED;
    } 
    else if (*cursor >= 'a' && *cursor <= 'z') {
        printf("%-16c F -> id\n", *cursor);
        cursor = match(cursor);
        return SUCCESS;
    } 
    else
        return FAILED;
}

