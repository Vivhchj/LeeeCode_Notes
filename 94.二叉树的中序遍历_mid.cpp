/*
给定一个二叉树，返回它的中序遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [1,3,2]
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */


 // 树的中序遍历的两种方法
 // Solution1：递归法
class Solution {
public:
    void recursion(TreeNode* node, vector<int> &result){
        if(node==nullptr){
            return ;
        }
        recursion(node->left, result);
        result.push_back(node->val);
        recursion(node->right, result);
    }

    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        if(root!=nullptr){
            recursion(root, result);
        }
        return result;
    }
};


//Solution2:迭代法
//1.从当前结点开始，找最深左子树，对经过的所有结点入栈，将最深左结点出栈，新一轮循环的根节点是当前出栈结点的右结点
//2.在新一轮循环中，若此右结点不为空，继续找最深左子树，操作同1
//3.在新一轮循环中，若此右结点为空，则取栈顶结点，出栈，下一轮循环的根节点是当前出栈结点的右结点
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        if(root==nullptr){
            return res;
        }
        TreeNode *cur = root;
        stack<TreeNode *> st;
        //当传入的cur或栈st不为空时
        while(cur || !st.empty()){
            //cur不为空时，入栈并继续搜索cur子树的最深左子树
            while(cur){
                st.push(cur);
                cur = cur->left;
            }
            //达到最深左子树后，加入输出数组res中,并出栈st
            cur = st.top();
            res.push_back(cur->val);
            st.pop();
            //不论是否为空，将当前结点的右结点赋给cur
            cur = cur->right;
        }
        return res;
    }
};
