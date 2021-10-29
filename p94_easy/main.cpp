#include<vector>
#include<iostream>
using namespace std;
struct TreeNode
{
    public:
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> result;
    vector<int> inorderTraversal(TreeNode* root) {
        result.clear();
        inorderWalk(root);
        return result;
    }

    void inorderWalk(TreeNode *root) {
        if (root == nullptr) {
            return;
        }
        if (root->left!=nullptr) {
            inorderWalk(root->left);
        }
        result.push_back(root->val);
        if (root->right!=nullptr) {
            inorderWalk(root->right);
        }
        return ;
    }
};

int main() {
    auto root = new TreeNode(1, nullptr, new TreeNode(2, new TreeNode(3), nullptr));
    auto test = Solution();
    auto res = test.inorderTraversal(root);
    for (auto item : res) {
        cout << item <<endl;
    }
    return 0;
}