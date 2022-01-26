/*
 * @lc app=leetcode id=235 lang=cpp
 *
 * [235] Lowest Common Ancestor of a Binary Search Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <vector>
using namespace std;
class Solution
{
private:
    void search(TreeNode* root, TreeNode* target, vector<TreeNode*>& route) {
        while (root != nullptr && target->val != root->val)
        {
            route.push_back(root);
            if (target->val < root->val) {
                root = root->left;
            } else {
                root = root->right;
            }
        }
        return; 
    }
public:
    TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q)
    {
        vector<TreeNode*> pRoute,qRoute;
        auto rr = root;
        search(rr, p, pRoute);
        pRoute.push_back(p);
        rr = root;
        search(rr, q, qRoute);
        qRoute.push_back(q);
        TreeNode* result = root;
        for(int i = 0; i <= min(pRoute.size()-1, qRoute.size()-1);++i){
            if (pRoute[i]->val == qRoute[i]->val) {
                result = pRoute[i];
            } else {
                break;
            }
        }
        return result;
    }
};
// @lc code=end
