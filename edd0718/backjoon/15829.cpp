#include <iostream>
#include <string>

#define r 31
#define M 1234567891

int main() {
    int l;
    std::cin >> l;
    
    std::string s;
    std::cin >> s;

    long long res = 0;
    long long temp = 1;

    for (int i=0; i<s.length(); i++) {
        res += ((s[i]-'a'+1) * temp) % M;
        temp *= r;
        temp %= M;
    }
    std::cout << res % M << std::endl;
}
