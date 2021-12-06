/*
 * @lc app=leetcode id=77 lang=cpp
 *
 * [77] Combinations
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <stack>
using namespace std;
class Solution
{
public:
    vector<vector<int>> combine(int n, int k)
    {
        vector<vector<int>> res;
        stack<vector<int>> poss;
        for (int i = 1; i <= n; ++i)
        {
            vector<int> temp;
            temp.push_back(i);
            poss.push(temp);
        }
        do {
            auto now = poss.top();
            poss.pop();
            if (now.size() == k)
            {
                res.push_back(now);
            } 
            else
            {
                for (auto i = now.back()+1; i <= n; ++i)
                {
                    vector<int> temp(now);
                    temp.push_back(i);
                    poss.push(temp);
                }
            }
        } while (!poss.empty());

        return res;
    }
};
// @lc code=end
