/*
 * @lc app=leetcode id=78 lang=cpp
 *
 * [78] Subsets
 */

// @lc code=start
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n = nums.size();
        vector<vector<int>> res;
        res.push_back({});
        for (auto i: nums) {
            res.push_back({i});
        }
        size_t head= 1;
        while (head < res.size())
        {
            auto top = res[head];
            if(top.size() < n) {
                auto startPos = find(nums.begin(),nums.end(),top.back())+1;
                for (auto p = startPos; p != nums.end();++p) {
                    vector<int> temp(top);
                    temp.push_back(*p);
                    res.push_back(temp);
                }
            }
            ++head;
        }
        return res;
    }
};
// @lc code=end

