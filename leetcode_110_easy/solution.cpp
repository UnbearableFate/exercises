#include<iostream>
#include<vector>
#include<tuple>
#include<algorithm>
#include "../my_lib/my_lib.h"
using namespace std;
typedef T_TreeNode<int> TreeNode;
class Solution {
public:
    tuple<int,bool > treeWalk(TreeNode* node) {
        int height, lh,rh;
        bool lb,rb;
        auto balanced = true;
        if(node == nullptr) {
            return std::tuple<int,bool>(0,true);
        }
        
        if (node->left != nullptr) {
            tie(lh,lb) = treeWalk(&*node->left);
        } else {
            lh = 0;
            lb = true;
        }

        if (node->right != nullptr) {
            tie(rh,rb) = treeWalk(&*node->right); 
        } else {
            rh = 0;
            rb = true;
        }

        if(abs(lh-rh)>1) {
            balanced = false;
        }

        height = max(lh,rh);
        balanced = lb && rb && balanced;
        return tuple<int, bool>(height, balanced);
    }
    bool isBalanced(TreeNode* root) {
        int useless;
        bool res;
        tie(useless, res) = treeWalk(root);    
        return res;
    }
};

int main(int argc, char** argv) {
    //auto mytree = Tree<int>({1,-1,3,2});
    auto root = make_shared<TreeNode>(TreeNode(1));
    auto a = make_shared<TreeNode>(TreeNode(3));
    auto b = make_shared<TreeNode>(TreeNode(2));
    root->right = a;
    a->left = b;
    auto ss = Solution();
    cout << ss.isBalanced(&*root)<<endl;
    return 0;
}
