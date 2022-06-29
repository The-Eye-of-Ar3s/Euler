#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>

int largest_prime_factor(long long int n) {
    int p = 2;
    while (n >= p*p) {
        if (n%p == 0) {
            n /= p;
        } else {
            p++;
        }
    }
    return n;
}

bool is_prime(int n) {
    if (n == 1) {
        return 0;
    }
    
    int i = 2;
    while (i*i <= n) {
        if (n%i == 0) {
            return 0;
        }
        i += 1;
    }
    return 1;
}

int is_palindromic(long num)
{
    long reverse=0,c_num;
    c_num=num;
    while(num)
    {
        reverse=(reverse*10)+(num%10);
        num/=10;
    }

    if(reverse==c_num) {
        return 1;
    }
    return 0;
}

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

int solve003() {
    return largest_prime_factor(600851475143);
}

int solve004() {
    unsigned int i, j, max = 0;
    for (i = 100; i <= 999; i++) {
        for (j = 100; j <= 999; j++) {
            unsigned int p = i*j;
            if (is_palindromic(p) && p > max) {
            max = p;
            }
        }
    }
    return max;
}

int solve006() {
    int n1 = 0;
    int n2 = 0;
    for (int i = 1; i <= 100; i++) {
        n1 += i*i;
        n2 += i;
    }
    n2 *= n2;
    return n2 - n1;
}

int solve007() {
    int i = 3;
    int p = 2;
    int c = 1;
    while (c != 10001) {
        if (is_prime(i)) {
            p = i;
            c+=1;
        }
        i+=2;
    }
    return p;
}

int main(int argc, char** argv) {
    switch(atoi(argv[1])) {
        case 1:
            printf("%d\n", solve001());
            break;
        case 2:
            printf("%d\n", solve002());
            break;
        case 3:
            printf("%d\n", solve003());
            break;
        case 4:
            printf("%d\n", solve004());
            break;
        case 6:
            printf("%d\n", solve006());
            break;
        case 7:
            printf("%d\n", solve007());
            break;
        default:
            printf("NA\n");
            break;
    }
    return 0;
}
