/*
 * @lc app=leetcode id=79 lang=cpp
 *
 * [79] Word Search
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class State
{
public:
    int posX = 0;
    int posY = 0;
    int color = 0;
    int depth = 0;
    vector<State *> children;
    State(int x, int y)
    {
    }
};

class Solution
{
public:
    bool search(int x, int y, int d, const string &word, const vector<vector<char>> &board, vector<vector<int>> &color)
    {
        color[x][y] =1;
        if (d == word.size() - 1 && board[x][y] == word[d])
        {
            return true;
        }
        vector<vector<int>> pos = {{x,y-1},{x,y+1},{x-1,y}, {x+1,y}};
        for (auto p : pos)
        {
            auto xx = p[0];
            auto yy = p[1];
            if (xx >= 0 && xx < board.size() && yy >= 0 && yy < board[0].size()
             && color[xx][yy] == 0 && board[xx][yy] == word[d + 1]
             &&search(xx, yy, d + 1, word, board, color))
            {
                return true;
            }
        }
        color[x][y] = 0;
        return false;
    }
    bool exist(vector<vector<char>> &board, string word)
    {
        if (word.size() == 0)
            return true;
        if (board.size() == 0)
            return false;
        for (int i = 0; i != board.size(); ++i)
        {
            for (int j = 0; j != board[0].size(); ++j)
            {
                if (board[i][j] == word[0])
                {
                    vector<vector<int>> color(board.size(), vector<int>(board[0].size(), 0));
                    color[i][j] = 1;
                    if (search(i, j, 0, word, board, color)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
};
// @lc code=end

int main()
{
    Solution ss;
    vector<vector<char>> ww = {
        {'A', 'A', 'A', 'A', 'A', 'A'},
        {'A', 'A', 'A', 'A', 'A', 'A'},
        {'A', 'A', 'A', 'A', 'A', 'A'},
        {'A', 'A', 'A', 'A', 'A', 'A'},
        {'A', 'A', 'A', 'A', 'A', 'A'},
        {'A', 'A', 'A', 'A', 'A', 'A'}
    };
    cout << ss.exist(ww, "AAAAAAAAAAAAAAB") << endl;
}