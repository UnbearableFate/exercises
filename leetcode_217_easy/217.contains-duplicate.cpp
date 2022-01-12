/*
 * @lc app=leetcode id=217 lang=cpp
 *
 * [217] Contains Duplicate
 */

// @lc code=start
#include<vector>
#include<map>
#include<algorithm>
#include<bitset>
using namespace std;
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        bitset bb;
        for (size_t i = 0; i < nums.size(); i++)
        {
            if(countMap.count(nums[i]) == 0) {
                countMap[nums[i]] = 1;
            } else
            {
                return true;
            }
        }
        return false; 
    }
};
// @lc code=end

