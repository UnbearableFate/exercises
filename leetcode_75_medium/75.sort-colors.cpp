/*
 * @lc app=leetcode id=75 lang=cpp
 *
 * [75] Sort Colors
 */

// @lc code=start
#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    void sortColors(vector<int>& nums) {
       int ct[3] = {0,0,0};
       for (auto i : nums) {
           ct[i]++;
        }
       for (int i =0; i < ct[0]; ++i) {
            nums[i] = 0;
       }
       for (int i =0; i < ct[1]; ++i) {
           nums[ct[0]+i] = 1;
       }
       for (int i =0; i < ct[2]; ++i) {
        nums[ct[0]+ct[1]+i] = 2;
        }
        return;
    }
};
// @lc code=end

int main(){
    vector<int> a = {2};
    Solution sss;
    sss.sortColors(a);
    for (auto c : a) {
        cout << c <<endl;
    }
}