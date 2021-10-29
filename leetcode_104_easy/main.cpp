struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int max;
    int treewalk(TreeNode *node, int depth)
    {
        if (node == nullptr) {
            return max;
        }
        ++depth;
        if (depth > max)
        {
            max = depth;
        }
        if (node->left == nullptr && node->right == nullptr)
        {
            return depth;
        }
        if (node->left != nullptr)
        {
            treewalk(node->left, depth);
        }
        if (node->right != nullptr)
        {
            treewalk(node->right, depth);
        }
        return max;
    }
    int maxDepth(TreeNode *root)
    {
        int d = 0;
        max = 0;
        treewalk(root,d);
        return max;
    }
};