/*
 * @lc app=leetcode id=91 lang=cpp
 *
 * [91] Decode Ways
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    int numDecodings(string s) {
        return search(s);
    }
    int search(string other) {
        if (other.size()==1) {
            if (int(other[0])-48 > 0) {
                return 1;
            } else {
                return 0;
            }
        }
        if (other.size() >=2) {
            int l,r =0;
            auto leftValue = int(other[0]) - 48;
            if (leftValue > 0) {
                auto left = other.substr(1,other.size()-1);
                l = search(left)+1;
            }
            auto rightValue = (int(other[0]) - 48)*10+(int(other[1]) - 48);
            if (rightValue>=10 && rightValue <= 26) {
                auto right = other.substr(2,other.size()-2);
                r = search(right)+1;
            }
            return max(l,r);
        }
        return 0;
    }
};
// @lc code=end

int main() {
    auto s = Solution();
    printf("%d", s.numDecodings("06"));
}