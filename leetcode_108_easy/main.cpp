#include <vector>
#include <iostream>

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

class Solution {
public:
    void getTree(vector<int>& nums, size_t p, size_t q, TreeNode *root) {
        if(p < q) {
            size_t inter = (q +p) /2;
            root = new TreeNode();
            root->val = nums[inter];
            getTree(nums, p, inter, root->left);
            getTree(nums, inter+1, q, root->right);
        }
        return;
    }
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        TreeNode *p;
        getTree(nums, 0, nums.size(),p);
        return p;
    }
};

int main() {
    vector<int> aa = {-10,-3,0,5,9};
    Solution ppp;
    auto p = ppp.sortedArrayToBST(aa);
    cout << p->val <<endl;
}

/*
 TreeNode* getTree(vector<int>& nums, size_t p, size_t q, TreeNode *root) {
        if(p < q) {
            size_t inter = (q +p) / 2;
            root = new TreeNode(nums[inter]);
            getTree(nums, p, inter, root->left);
            getTree(nums, inter+1, q, root->right);
        }
        return root;
    }
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        TreeNode *p ;
        return getTree(nums, 0, nums.size(),p);
    }
*/