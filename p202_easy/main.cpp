#include <iostream>
#include <set>
using namespace std;

class Solution {
public:
    bool isHappy(int n) {
        set<int>ok = {1,7,10,13,19,23,28,31,32,44,49,68,70,79,82,86,91,94,97}; 
        set<int> results;
        do
        {
            results.insert(n);
            n = this->oneLoop(n);
            if (n == 1) {
                return true;
            }
            
        } while (results.count(n) != 1);
        
        return false;
    }

    int oneLoop(int n) {
        int res = 0;
        while (n != 0)
        {
            int c = n % 10;
            res  += c * c;
            n = (n - c) / 10;
        }
        return res;
    }
};


int main() {
    auto test = Solution();
    for(int i = 1; i < 1000 ;++i) {
        if (test.isHappy(i)) {
            std::cout << i <<",";
        }
    }
    cout <<endl;
    return 0;
}