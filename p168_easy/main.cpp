#include<functional>
#include<iostream>
#include<string>
using namespace std;
class Solution {
public:
    string convertToTitle(int columnNumber) {
        string res = "";
        while (columnNumber > 0)
        {
            int tail = columnNumber % 26;
            if (tail == 0)
            {
                res = 'Z'+res;
                columnNumber = (columnNumber - 26) /26;
            } else {
                res = char(tail+64) +res;
                columnNumber = columnNumber/ 26;
            }
        }
        return res;
    }
};
int foo (int x, int y) {
    return x*2*y;
}
int main() {
    auto ss = Solution();
    auto a = [&] (auto c) {
        return ss.convertToTitle(c);
    };
    auto ww = foo;
    auto bindFoo = std::bind(ww, placeholders::_1,2);
    cout << bindFoo(2)<<endl;
}