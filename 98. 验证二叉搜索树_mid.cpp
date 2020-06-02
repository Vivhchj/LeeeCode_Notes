/*
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

示例 1: [-2147483648,-2147483648] ([INT_MIN, INT_MIN])
输入:
    INT_MIN
     /
  INT_MIN
输出: false

示例 2:
输入: [5,1,4,null,null,3,6]。
    5
   / \
  1   4
     / \
    3   6
输出: false
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

//二叉搜索树的中序遍历一定是有序的
//Solution1:递归法
class Solution {
public:
    void inOrder(TreeNode *node, vector<int> &vt){
        if(node==nullptr){
            return ;
        }
        inOrder(node->left, vt);
        vt.push_back(node->val);
        inOrder(node->right, vt);
    }

    //直接中序遍历并加入数组，看是否满足严格递增顺序
    bool isValidBST(TreeNode* root) {
        if(root==nullptr){
            return true;
        }
        vector<int> vt;
        bool res = true;
        inOrder(root, vt);
        //检查st是否有序
        for(int i=0; i<vt.size()-1; ++i){
            //必须严格递增
            if(vt[i]>=vt[i+1]){
               res = false;
               break; 
            }
        }
        return res;
    }
};


//Solution2:迭代法
class Solution {
public:
    //直接中序遍历入栈，看是否满足即将入栈的值大于当前栈顶stack.top()
    bool isValidBST(TreeNode* root) {
        if(root==nullptr){
            return true;
        }
        //用栈模拟递归
        stack<TreeNode *> st;
        stack<int> seq;
        TreeNode *cur = root;
        bool result = true;
        while(cur || !st.empty()){
            // 遍历到最深左子树结点，沿途结点入栈
            while(cur!=nullptr){
                st.push(cur);
                cur = cur->left;
            }
            //当前栈顶为当前最小结点，出栈并且指向右结点
            cur = st.top();
            st.pop();
            //判断是否满足严格递增，满足则入排序栈
            if(seq.empty() || cur->val > seq.top()){
                seq.push(cur->val);
            }
            else{
                result = false;
                break;
            }
            cur = cur->right;
        }
        return result;
    }
};
