#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if (obstacleGrid.size() == 0 || obstacleGrid[0].size() == 0) {
            return 0;
        }
        if (obstacleGrid[obstacleGrid.size()-1][obstacleGrid.begin()->size()-1] == 1) {
            return 0;
        }
        obstacleGrid[0][0] = -1;
        for(int i = 0 ; i < obstacleGrid.size();++i) {
            for (int j = 0; j < obstacleGrid[0].size(); ++j) {
                if (i==0 && j==0) {
                    continue;
                }
                if (obstacleGrid[i][j] == 1){
                    continue;
                }
                int up=0 ;
                int left=0 ;
                if (i-1 >= 0 && obstacleGrid[i-1][j] != 1) {
                    up = obstacleGrid[i-1][j];
                }
                if (j-1 >= 0 && obstacleGrid[i][j-1] != 1) {
                    left = obstacleGrid[i][j-1];
                }
                obstacleGrid[i][j] = up + left;
            }
        }
        return -obstacleGrid[obstacleGrid.size()-1][obstacleGrid.begin()->size()-1];
    }
};

int main() {
    auto ss = Solution();
    vector<vector<int>> test = {
        {0,0,0},{0,1,0},{0,0,0}
    };
    cout << ss.uniquePathsWithObstacles(test) <<endl;
}