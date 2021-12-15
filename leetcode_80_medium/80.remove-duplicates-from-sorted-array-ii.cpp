/*
 * @lc app=leetcode id=80 lang=cpp
 *
 * [80] Remove Duplicates from Sorted Array II
 */

// @lc code=start
#include <vector>
#include <iostream>
using namespace std;
class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        int i = 0;
        int ct = 0;
        int k = nums.size();
        while (i+2 < nums.size())
        {
            int num = nums[i];
            ct = 1;
            for (int j = i+1;j < nums.size();++j) {
                if (nums[j] == num)
                {
                    ct++;
                    if (ct > 2)
                    {
                        nums.erase(nums.begin() + j);
                        k--;
                        j--;
                    }
                } else {
                    i = j;
                    break;
                }
            }
        }
        return k;
    }
};
// @lc code=end
int main() {
    auto ss = Solution();
    vector<int> v = {0,0,1,1,1,1,2,3,3};
    cout << ss.removeDuplicates(v) << endl;
    for (auto a :v) {
        cout << a << " , ";
    }
    cout <<endl;
}