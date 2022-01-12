/*
 * @lc app=leetcode id=219 lang=cpp
 *
 * [219] Contains Duplicate II
 */

#include<map>
#include<vector>
#include<cmath>
using namespace std;
// @lc code=start
class Solution {
public:
    int myAbs(int a) {
        if (a >=0) {
            return a;
        } else
        {
            return -a;
        }
        
    }
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int, size_t> hashMap;
        for(size_t i =0; i != nums.size();++i) {
            int n = nums[i];
            if(hashMap.count(n) == 0) {
                hashMap[n] = i;
            } else
            {
                if (myAbs(hashMap[n]-i) <= k) {
                    return true;
                } else
                {
                    hashMap[n] = i;
                }
            }
        }
        return false;        
    }
};
// @lc code=end

