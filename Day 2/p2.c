#include <stdio.h>
#include <string.h>

int main () {

    FILE *input = fopen("input.txt", "r");
    int i = 0;
    const int SIZE = 1000;
    int inNum1[SIZE];
    int inNum2[SIZE];
    char inAlpha[SIZE];
    int count = 0;

    //2d array for storing array of strings
    char inPass[SIZE][1000];

    while ((fscanf(input, "%d-%d %c: %s", &inNum1[i], &inNum2[i], &inAlpha[i], inPass[i])) != EOF) {
        i++;
        count++;
    }

    int num = 0;

    for(i = 0; i < count; i++) {
            if ((inPass[i][inNum1[i] - 1] == inAlpha[i] && inPass[i][inNum2[i] - 1 ] != inAlpha[i]) || (inPass[i][inNum2[i] - 1 ] == inAlpha[i] && inPass[i][inNum1[i] - 1] != inAlpha[i])) {
            num++;
        }
    }

    printf("%d passwords are valid!\n", num);
    return 0;
}//end of main