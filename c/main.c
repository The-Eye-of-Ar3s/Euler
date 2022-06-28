#include <stdio.h>
#include <stdlib.h>

int solve001() {
    int s = 0;
    for (int i = 1; i < 1000; i++) {
        if (i%3 == 0 || i%5 == 0) {
            s+=i;
        }
    }
    return s;
}

int solve002() {
    int s = 0;
    int first = 1;
    int second = 2;
    int temp;
    while (second < 4000000) {
        if (second%2 == 0) {
            s+=second;
        }
        temp = first;
        first = second;
        second += temp;
    }
    if (second%2==0) {
        s-=second;
    }
    return s;
}

int main(int argc, char** argv) {
    switch(atoi(argv[1])) {
        case 1:
            printf("%d\n", solve001());
            break;
        case 2:
            printf("%d\n", solve002());
            break;
        default:
            printf("NA\n");
            break;
    }
    return 0;
}
