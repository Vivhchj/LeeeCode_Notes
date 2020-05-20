// contens:
// 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

// 示例:
// 输入:
// [
  // ["1","0","1","0","0"],
  // ["1","0","1","1","1"],
  // ["1","1","1","1","1"],
  // ["1","0","0","1","0"]
// ]
// 输出: 6

// Solution1:按行遍历，每个位置记录能往前延伸的长度（连续1的长度）；
//          按列遍历整个矩阵，以当前点作为矩阵右下角，从下往上遍历，每个点作为矩阵右上角举行
#include <algorithm>
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if(matrix.size() == 0){
            return 0;
        }
        int row = matrix.size(), col = matrix[0].size();
        vector<vector<int> > map(row, vector<int> (col, 0));
        // 按行遍历，将矩阵每一个元素值改为连续1的长度
        for(int i = 0; i < row; ++i){
            map[i][0] = matrix[i][0] - '0';
            for(int j = 1; j < col; ++j){
                if(matrix[i][j] != '0'){
                    map[i][j] = 1 + map[i][j-1];
                }
            }
        }
        int min_W, max_S = 0;
        // 按列遍历，求以matrix[i][j]为右下角的面积最大矩形
        for(int j = 0; j < col; ++j){
            for(int i = 0; i < row; ++i){
                min_W = col;
                //更新min_W
                for(int k = i; k >= 0; --k){
                    if(map[k][j] == 0){
                        break;
                    }
                    //min_W = map[k][j] < min_W? map[k][j] : min_W;
                    min_W = min(map[k][j], min_W);
                    //max_S = max_S > min_W*(i-k+1)? max_S : min_W*(i-k+1);
                    max_S = max(max_S, min_W*(i-k+1));
                }
            }
        }
        return max_S;
    }
};

// Solution2:按行划分，每一行及其以上的部分看作84题寻找最大矩形面积问题；
#include<algorithm>
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if(matrix.size()==0){
            return 0;
        }
        int row = matrix.size(), col = matrix[0].size();
        stack<int> s;
        s.push(-1);
        vector<int> h(col, 0);
        int height = 0, max_S = 0;
        for(int i = 0; i < row; ++i){
            // 更新h[j]，并进行栈的操作
            while(s.top()!=-1){
                s.pop();
            }
            for(int j =0; j < col; ++j){
                if(matrix[i][j] == '1'){
                    h[j] += 1;
                }
                else{
                    h[j] = 0;
                }
                // 利用栈求面积
                while(s.top()!=-1 && h[s.top()]>h[j]){
                    height = h[s.top()];
                    s.pop();
                    max_S = max(max_S, height*(j-s.top()-1));
                }
                s.push(j);
            }
            while(s.top()!=-1){
                height = h[s.top()];
                s.pop();
                max_S = max(max_S, height*(col-s.top()-1));
            }
            
        }
        return max_S;
    }
};
