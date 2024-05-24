#include <stdio.h>

int main() {
    char file_name[100];
    FILE *file;
    char ch;
    int char_count = 0, space_count = 0, line_count = 0, tab_count = 0;

    printf("Enter the file name: ");
    scanf("%s", file_name);

    file = fopen(file_name, "r");

    if (file == NULL) {
        printf("File not found or path is incorrect.\n");
        return 1;
    }

    while ((ch = fgetc(file)) != EOF) {
        char_count++;
        if (ch == ' ')
            space_count++;
        if (ch == '\t')
            tab_count++;
        if (ch == '\n')
            line_count++;
    }

    fclose(file);

    if (char_count > 0)
        line_count++;

    printf("Characters: %d\n", char_count);
    printf("Spaces: %d\n", space_count);
    printf("Lines: %d\n", line_count);
    printf("Tabs: %d\n", tab_count);

    return 0;
}
