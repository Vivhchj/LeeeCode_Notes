/*
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:
输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
*/

//Solution:动态规划
//总结数学规律，G(n)=Σ F(1,i-1)*F(i+1,n) i=1,...,n，F(i,n)=G(i-1)*G(n-i)，详见官方题解
//https://leetcode-cn.com/problems/unique-binary-search-trees/solution/bu-tong-de-er-cha-sou-suo-shu-by-leetcode/
class Solution {
public:
    int numTrees(int n) {
        if(n==0 || n==1){
            return 1;
        }
        //创建一个数组存储G(n)
        vector<int> num{1,1};
        int temp;
        for(int i=2; i<=n; ++i){
            //计算G(i)存到temp
            temp = 0;
            for(int j = 1; j<=i; ++j){
                temp += num[j-1]*num[i-j];
            }
            num.push_back(temp);
        }
        return num.back();
    }
};
