/*
 * @lc app=leetcode id=263 lang=cpp
 *
 * [263] Ugly Number
 */

// @lc code=start
class Solution {
public:
    bool isUgly(int n) {
       if (n == 1 ) {
           return true;
       } 
       while (true)
       {
           if (n%2 == 0) {
               n = n /2;
               continue;
           }
           if (n%3 == 0) {
               n = n /3;
               continue;
           }
           if (n%5 == 0) {
               n = n /5;
               continue;
           }
           if (n == 1) {
               return true;
           } else
           {
               return false;
           }
       }
    }
};
// @lc code=end

