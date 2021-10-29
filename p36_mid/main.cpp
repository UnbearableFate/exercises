#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution
{

public:
    bool isValidSudoku(vector<vector<char>> &board)
    {
        vector<unordered_set<char>> rowSet(9);
        vector<unordered_set<char>> colSet(9);
        vector<unordered_set<char>> blockSet(9);
        for (int i = 0; i < 9; ++i)
        {
            for (int j = 0; j < 9; ++j)
            {
                if (board[i][j] == '.')
                {
                    continue;
                }
                auto rres = rowSet[i].insert(board[i][j]);
                if (!rres.second) {
                    return false;
                }
                auto cres = colSet[j].insert(board[i][j]);
                if (!cres.second) {
                    return false;
                }
                auto bres = blockSet[(i / 3) * 3 + (j / 3)].insert(board[i][j]);
                if (!bres.second) {
                    return false;
                }
            }
        }
        return true;
    }
};

int main()
{
    auto ss = Solution();

    vector<vector<char>> test = {
        {'8', '3', '.', '.', '7', '.', '.', '.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}};
    cout << ss.isValidSudoku(test) << endl;
    return 0;
}