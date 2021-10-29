#include<iostream>
#include<string>
#include<vector>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        vector<char> str;
        for(auto c :s ) {
            if(c != ' ' || ',') {
               str.push_back(c); 
            }
        }
        if(str.size() % 2 == 0) {
            int mid = str.size() / 2;
            for(int i = 0; i <= mid; ++i) {
                if(str[i] != str[str.size()-1-i]) {
                    return false;
                }
            }
        }else {
            int mid = str.size() /2 ;
            for(int i = 0; i < mid ; ++i) {
                if(str[i] != str[str.size()-1-i]) {
                    return false;
                }
            }
        }
        return true;
    }
};

int main() {
    auto ss = Solution()
    cout << ss.isPalindrome("")
} 
