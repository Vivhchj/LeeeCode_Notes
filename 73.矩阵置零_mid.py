# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

# 示例 1:
# 输入: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_num, col_num = len(matrix), len(matrix[0])
        # 创建集合set()用于存放需要置零的行和列
        row_set, col_set = set(), set()
        for row in range(row_num):
            for col in range(col_num):
                if matrix[row][col]==0:
                    row_set.add(row)
                    col_set.add(col)
        # 将记录的行、列中的元素赋值为0
        # 再次遍历赋值
        for row in range(row_num):
            for col in range(col_num):
                if row in row_set or col in col_set:
                    matrix[row][col] = 0
        # # 或者行列单独赋值均可
        # for row in row_set:
        #     for col in range(col_num):
        #         matrix[row][col] = 0
        # for col in col_set:
        #     for row in range(row_num):
        #         matrix[row][col] = 0
