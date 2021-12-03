/*
 * @lc app=leetcode id=73 lang=cpp
 *
 * [73] Set Matrix Zeroes
 */

// @lc code=start
#include<vector>
using namespace std;
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        if(matrix.size() == 0) {
            return;
        }
        int n = matrix.size();
        int m = matrix.begin()->size();
        vector<int> tag(matrix.size()*matrix.begin()->size());
        for (int i =0; i < matrix.size(); ++i) {
            for (int j = 0; j < matrix.begin()->size(); ++j) {
                if (matrix[i][j] == 0 && tag[i*m+j] ==  0) {
                    for (int k = 0; k < m ;++k) {
                        if (matrix[i][k] != 0 && tag[i*m+k] == 0) {
                            ++tag[i*m+k];
                        }
                        matrix[i][k] = 0;
                    }
                    for (int k = 0; k < n ;++k) {
                        if (matrix[k][j] != 0 && tag[k*m+j] == 0) {
                            ++tag[k*m+j];
                        }
                        matrix[k][j] = 0;
                    }
                }
            }
        }
    }
};
// @lc code=end

