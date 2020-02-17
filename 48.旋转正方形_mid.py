# 给定一个 n × n 的二维矩阵表示一个图像。将图像顺时针旋转 90 度。
# 说明：必须在原地旋转图像，这意味着需要直接修改输入的二维矩阵。不要使用另一个矩阵来旋转图像。

# 示例 1:
# 给定 matrix = 
# [
  # [1,2,3],
  # [4,5,6],
  # [7,8,9]
# ],
# 原地旋转输入矩阵，使其变为:
# [
  # [7,4,1],
  # [8,5,2],
  # [9,6,3]
# ]

# 示例 2:
# 给定 matrix =
# [
  # [ 5, 1, 9,11],
  # [ 2, 4, 8,10],
  # [13, 3, 6, 7],
  # [15,14,12,16]
# ], 
# 原地旋转输入矩阵，使其变为:
# [
  # [15,13, 2, 5],
  # [14, 3, 4, 1],
  # [12, 6, 8, 9],
  # [16, 7,10,11]
# ]

### Solution:由外向内旋转正方形框
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        a, b, c, d = 0, 0, 0, 0
        # 方框个数
        for i in range(n//2):
            # 方框边长-1
            for j in range(n-2*i-1):
                # 四个相关联的位置分别是
                # a = matrix[i][i+j]
                # b = matrix[i+j][n-1-i]
                # c = matrix[n-1-i][n-1-i-j]
                # d = matrix[n-1-i-j][i]
                # 顺序赋值d=temp;d=c,c=b,b=a;a=temp.
                temp = matrix[n-1-i-j][i]
                matrix[n-1-i-j][i] = matrix[n-1-i][n-1-i-j]
                matrix[n-1-i][n-1-i-j] = matrix[i+j][n-1-i]
                matrix[i+j][n-1-i] = matrix[i][i+j]
                matrix[i][i+j] = temp

### Solution2：先转置(沿主对角线翻折，使第n行变成第n列)，再左右翻转，第i列变成第n-i列
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 矩阵转置，matrix[i][j]下标互换
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 左右翻转
        for i in range(n//2):
            for j in range(n):
                matrix[j][i], matrix[j][n-1-i] = matrix[j][n-1-i], matrix[j][i]
 
