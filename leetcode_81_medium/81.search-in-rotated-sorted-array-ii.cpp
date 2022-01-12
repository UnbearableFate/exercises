/*
 * @lc app=leetcode id=81 lang=cpp
 *
 * [81] Search in Rotated Sorted Array II
 */

// @lc code=start
#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    bool search(vector<int> &nums, int target)
    {
        if (nums.size() == 0) {
            return false;
        }
        if (nums.size() == 1) {
            return nums[0] == target;
        }

        if (nums[0] <= target)
        {
            size_t i = 0;
            do {
                if (nums[i] == target || nums[i + 1] == target)
                {
                    return true;
                }

                if (nums[i] < target && target < nums[i + 1]) {
                    return false;
                }
                ++i;
            } while (i< nums.size()-1 && nums[i-1] <= nums[i]);
            
        } else
        {
            size_t i = nums.size()-1;
            do {
                if (nums[i] == target || nums[i-1] == target)
                {
                    return true;
                }
                if(nums[i-1] < target && target < nums[i]) {
                    return false;
                }
                --i;
            } while(i>= 1 && nums[i] <= nums[i+1]);
        }
        return false;
    }
};
// @lc code=end
int main() {
    auto ss = Solution();
    vector<int> test = {1,1};
    cout << ss.search(test,2) <<endl;
}