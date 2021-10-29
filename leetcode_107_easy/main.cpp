#include <vector>
#include <stack>
#include <map>
using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    vector<vector<int>> levelOrderBottom(TreeNode *root)
    {
        if (root == nullptr)
        {
            vector<vector<int>> result;
            return result;
        }
        stack<pair<TreeNode *, int>> treewalkStack;
        map<int, vector<int>> depthLevelMap;
        treewalkStack.push(make_pair(root, 1));
        while (!treewalkStack.empty())
        {
            auto temp = treewalkStack.top();
            depthLevelMap[temp.second].push_back(temp.first->val);
            treewalkStack.pop();
            if (temp.first->right != nullptr)
            {
                treewalkStack.push(make_pair(temp.first->right, temp.second + 1));
            }
            if (temp.first->left != nullptr)
            {
                treewalkStack.push(make_pair(temp.first->left, temp.second + 1));
            }
        }
        vector<vector<int>> result;
        for (map<int, vector<int>>::reverse_iterator rit = depthLevelMap.rbegin(); rit != depthLevelMap.rend(); rit++)
        {
            result.push_back(rit->second);
        }
        return result;
    }
};