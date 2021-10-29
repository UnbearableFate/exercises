#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& grid) {
        if (grid.size() == 0 || grid[0].size() == 0) {
            return 0;
        }
        if (grid.size() == 1 && grid.begin()->size() ==1) {
            return grid[0][0];
        }
        for(int i = 0 ; i < grid.size();++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (i==0 && j==0) {
                    continue;
                }
                int up=grid[i][j];
                int left=grid[i][j];
                if (i-1 >= 0) {
                    up += grid[i-1][j];
                } else {
                    up = INT32_MAX;
                }
                if (j-1 >= 0) {
                    left += grid[i][j-1];
                } else {
                    left = INT32_MAX;
                }
                grid[i][j] = min(up,left);
            }
        }
        return grid[grid.size()-1][grid.begin()->size()-1];
    }

    int minPathSum(vector<vector<int>>& grid) {

    }

    int gogogo(vector<vector<int>>& grid, int i, int j) {
        
    }

};

int main() {
    auto ss = Solution();
    vector<vector<int>> test = {
        {1,3,1},{1,5,1},{4,2,1}
    };
    cout << ss.uniquePathsWithObstacles(test) <<endl;
}