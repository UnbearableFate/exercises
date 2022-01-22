/*
 * @lc app=leetcode id=268 lang=cpp
 *
 * [268] Missing Number
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    int missingNumber(vector<int>& nums) {
       int sum = 0;
       for (int a : nums)
       {
           sum += a;
       }
       return nums.size()*(nums.size()+1)/2 - sum;
    }
};
// @lc code=end

