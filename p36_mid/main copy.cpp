#include <iostream>
#include <vector>
#include <tuple>
#include <map>
#include <queue>
#include <memory>
using namespace std;

class State
{
private:
    vector<vector<int>> table;
    tuple<size_t, size_t> currentPos;
    vector<int> possibleNumList;
    queue<shared_ptr<State>> childStates;
    shared_ptr<State> parentState;

public:
    State(vector<vector<char>> &board)
    {
        for (auto line : board)
        {
            this->table.push_back(vector<int>());
            auto p = this->table.back();
            for (auto ch : line)
            {
                if (ch == '.')
                {
                    p.push_back(0);
                }
                else
                {
                    p.push_back(int(ch) - 48);
                }
            }
        }
    }

};

class Solution
{
public:
    bool isValidSudoku(vector<vector<char>> &board)
    {
    }
};