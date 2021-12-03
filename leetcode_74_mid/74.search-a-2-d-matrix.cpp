/*
 * @lc app=leetcode id=74 lang=cpp
 *
 * [74] Search a 2D Matrix
 */

// @lc code=start
#include<vector>
#include<iostream>
using namespace std;
class Solution {
    private:
    int n,m;
    bool res=false;
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty()) {
            return false;
        }
        n= matrix.size();
        m = matrix[0].size();
        search(0, n*m,target, matrix);
        return res;
    }

    int search(size_t beg, size_t end,int target, vector<vector<int>>& matrix) {
        if (end-beg <= 1) {
            res = (matrix[beg/m][beg%m] == target);
            return beg;
        } else {
            int mid = (beg+end)/2;
            if(target>=matrix[mid/m][mid%m]) {
                return search(mid, end, target, matrix);
            } else {
                return search(beg, mid, target, matrix);
            }
        }
        return 0;
    }
};
// @lc code=end

int main() {
    vector<vector<int>> a{
        {1,2,3},
        {4,5,6}
    };
    auto s = Solution();
    cout << s.searchMatrix(a, 4) <<endl;
    return 0;
}