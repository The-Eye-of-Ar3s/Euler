#include <iostream>
#include <string>
using namespace std;


int solve001() {
    int s = 0;
    for (int i = 1; i < 1000; i++) {
        if (i%3 == 0 || i%5 == 0) {
            s+=i;
        }
    }
    return s;
}


int main(int argc, char** argv) {
    switch(stoi(argv[1])) {
        case 1:
            std::cout<<solve001()<<"\n";
            break;
        default:
            std::cout<<"NA\n";
            break;
    }
    return 0;
}