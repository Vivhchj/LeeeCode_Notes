# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

# 示例 1:
# 输入:
# [
 # [ 1, 2, 3 ],
 # [ 4, 5, 6 ],
 # [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]

# 示例 2:
# 输入:
# [
  # [1, 2, 3, 4],
  # [5, 6, 7, 8],
  # [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]

### Solution:
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        # 行索引
        i, m = 0, len(matrix)-1
        if m==-1: return result
        # 列索引
        j, n = 0, len(matrix[0])-1
        # 行操作
        def add_row(idx, start, stop, sign):
            for k in range(start, stop, sign):
                result.append(matrix[idx][k])
        # 列操作
        def add_col(idx, start, stop, sign):
            for k in range(start, stop, sign):
                result.append(matrix[k][idx])

        # m, n分别代表行数-1和列数-1
        # 每次螺旋的矩形边长左上和右下的坐标分别是(i, j)(m-i, n-j)
        # 四边等长加载，每条边加载长度为边长-1，范围range(j,n-j,1);range(i,m-i,1);range(n-j,j,-1);range(m-i,i,-1)
        # 当i<=m-i或j<=n-j时，所有的闭合外圈均遍历结束；可能还有单独的一行/列遗留，需要判断并输出
        while i<m-i and j<n-j:
            # 添加行，正序
            add_row(i, j, n-j, 1)
            # 添加列，正序
            add_col(n-j, i, m-i, 1)
            # 添加行，反序
            add_row(m-i, n-j, j, -1)
            # 添加列， 倒序
            add_col(j, m-i, i, -1)
            i += 1
            j += 1
        # 若索引相同，必有此行/列遗留
        if i==m-i:
            add_row(i, j, n-j+1, 1)
        elif j==n-j:
            add_col(n-j, i ,m-i+1, 1)
        return result

### Solution2: 逆时针旋转法：每次去掉第一行后都将剩下的矩阵逆时针旋转一圈
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            # '+'号与list.extend()功能相同
            res += matrix.pop(0)
            
            # map(function, iterable, ...) 根据提供的函数对指定序列做映射
            # 参数function表示映射函数，后面的参数代表一个或多个序列
            # function以参数序列中的每一个元素调用function函数，返回包含每次function函数返回值的map对象
            
            # zip()将可迭代的对象作为参数，将对象中元素一一打包成一个个元组，然后返回由这些元组组成的对象
            # zip()将对象看作一维，zip(*)可将二维列表看作矩阵形态，从而将同一维(列)的元素打包成一个元祖
            # list(zip([[1,2],[3,4]]))=[([1,2],),([3,4],)]; 
            # list(zip(*[[1,2],[3,4]]))=[(1,3),(2,4)]

            # [::-1]表示倒序，[[1,2],[3,4]]->[[3,4],[1,2]]
            matrix = list(map(list, zip(*matrix)))[::-1]
        return res
            
