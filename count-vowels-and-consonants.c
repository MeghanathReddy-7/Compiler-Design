#include<stdio.h>
#include<string.h>

int main() {
    char s[100];
    printf("Enter the string:");
    scanf("%s",&s);
    int i,vowels=0,consonants=0;
    for(i=0;i<strlen(s);i++)
    {
        if(isalpha(s[i]))
        {
            if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u')
            {
                vowels+=1;
            }
            else
            {
                consonants+=1;
            }
        }
    }
    printf("Number of vowels:%d\n",vowels);
    printf("Number of consonants:%d\n",consonants);
}
