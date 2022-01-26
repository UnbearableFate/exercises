/*
 * @lc app=leetcode id=228 lang=cpp
 *
 * [228] Summary Ranges
 */

// @lc code=start
#include<vector>
#include<string>
using namespace std;
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> result;
        int beg = 0;
        if(nums.empty()) return result;
        for (int i = beg; i != nums.size()-1;++i) {
            if (nums[i+1] > nums[i]+1) {
                if (nums[beg] == nums[i]) {
                    result.push_back(to_string(nums[beg]));
                }
                else
                {
                    result.push_back(to_string(nums[beg])+"->"+ to_string(nums[i]));
                }
                beg = i+1;
            } 
        }
        if (beg == nums.size()-1) {
            result.push_back(to_string(nums[beg]));
        }
        else
        {
            result.push_back(to_string(nums[beg])+"->"+ to_string(nums[nums.size()-1]));
        }
        return result;
    }
};
// @lc code=end

