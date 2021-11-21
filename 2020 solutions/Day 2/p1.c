#include <stdio.h>
#include <string.h>

int main () {

    FILE *input = fopen("input.txt", "r");
    int i = 0;
    const int SIZE = 1000;
    int inNum1[SIZE];
    int inNum2[SIZE];
    char inAlpha[SIZE];

    //2d array for storing array of strings
    char inPass[SIZE][1000];

    while ((fscanf(input, "%d-%d %c: %s", &inNum1[i], &inNum2[i], &inAlpha[i], inPass[i])) != EOF) {
        i++;
    }

    int j;
    int num = 0;

    for(i = 0; i < SIZE; i++) {
        int count = 0;

        for(j = 0; j < strlen(inPass[i]); j++) {
            //count the char inAlpha in inPass
            if(inPass[i][j] == inAlpha[i]) {
                count = count + 1;
            }
        }
    
        //if count is in between inNum1 and inNum2, then the password is valid.
        if(inNum1[i] <= count && count <= inNum2[i]) {
            num++;
        }
    }
    printf("%d passwords are valid!\n", num);
    return 0;
}//end of main