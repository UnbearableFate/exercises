/*
 * @lc app=leetcode id=205 lang=cpp
 *
 * [205] Isomorphic Strings
 */
#include<string>
#include <stdio.h>
#include <string.h>
using namespace std;

// @lc code=start
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        char charMap[128];
        bool pool[128];
        memset(charMap, 0,sizeof(charMap));
        memset(pool, 0,sizeof(pool));
        for(size_t i = 0 ; i != s.size();++i){
            auto key = static_cast<int>(s[i]);
            if(charMap[key] == 0){
                if (pool[t[i]] == 0) {
                    charMap[key] = t[i];
                    pool[t[i]] = 1;
                }
                else
                {
                    return false;
                }
                
            } 
            else
            {
                if (charMap[key] != t[i]) {
                    return false;
                }
            }
            
        }
        return true;
    }
};
// @lc code=end

int main() {
    auto ss = Solution();
    printf("answer: %d\n",ss.isIsomorphic("badc","baba"));
    printf("answer: %d\n",ss.isIsomorphic("paper","title"));
}