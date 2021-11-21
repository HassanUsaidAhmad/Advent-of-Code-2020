#include <stdio.h>

int main () {

    FILE *input = fopen("input.txt", "r");
    const int SIZE = 200;
    int inputArray[SIZE];

    int i = 0;

    while (fscanf(input, "%d", &inputArray[i]) != EOF) {        
        i++;
    }
    
    fclose(input);

    for (i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            for (int k = 0; k < SIZE; k++) {
                if (2020 - inputArray[k] - inputArray[j] == inputArray[i]) {
                    printf("The num is = %d\n", inputArray[i] * inputArray[j] * inputArray[k]);
                    break;
                }//end of if statement
            }//end of for loop k
        }//end of for loop j
    }//end of for loop i

    return 0;
}//end of main
