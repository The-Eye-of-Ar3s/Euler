#include <iostream>
#include <string>
#include <vector>

using namespace std;


std::vector<int> prime_factorize(long long int n) {
    vector<int> r;
    int p = 2;
    while (n >= p*p) {
        if (n%p == 0) {
            r.push_back(p);
            n /= p;
        } else {
            p++;
        }
    }
    r.push_back(n);
    return r;
}

void reverseStr(string& str)
{
    int n = str.length();
    for (int i = 0; i < n / 2; i++)
        swap(str[i], str[n - i - 1]);
}

int is_palindrome(int n) {
    std::string s = std::to_string(n);
    std::string rs = s;
    reverseStr(rs);
    if (s == rs) {
        return 1;
    } else {
        return 0;
    }
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
    vector<int> fib;
    fib.push_back(1);
    fib.push_back(2);
    while (fib[fib.size()-1] < 4000000) {
        fib.push_back(fib[fib.size()-1]+fib[fib.size()-2]);
    }
    fib.pop_back();
    for(auto & i : fib) {
        if (i%2 == 0) {
            s+=i;
        }
    }
    return s;
}

int solve003() {
    vector<int> pf = prime_factorize(600851475143);
    int s = pf.size()-1;
    return pf[s];
}

int solve004() {
    int m = 0;
    int ml;
    for (int i = 999; i > 100; i--) {
        for (int j = i; j > 100; j--) {
            ml = i*j;
            if (is_palindrome(ml) && ml>m) {
                m = ml;
            }
        }
    }
    return m;
}

int main(int argc, char** argv) {
    switch(stoi(argv[1])) {
        case 1:
            std::cout<<solve001()<<"\n";
            break;
        case 2:
            std::cout<<solve002()<<"\n";
            break;
        case 3:
            std::cout<<solve003()<<"\n";
            break;
        case 4:
            std::cout<<solve004()<<"\n";
            break;
        default:
            std::cout<<"NA\n";
            break;
    }
    return 0;
}