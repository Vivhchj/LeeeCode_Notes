# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 问总共有多少条不同的路径？
# 说明：m 和 n 的值均不超过 100。

# 示例 1:
# 输入: m = 3, n = 2
# 输出: 3
# 解释: 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右

### Solution1：递归（超时）
### 思想，由起点按照向下向右两个方向进行遍历，每个点返回从该点到终点的所有路径数
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def move(mi, ni):
            if mi==m-1 or ni==n-1:
                return 1
            return (move(mi+1, ni) if mi+1<m else 0) + (move(mi, ni+1) if ni+1<n else 0)
        return move(0, 0)

### Solution2：数学规律：根据网格路径，要向下走m-1步，向右走n-1步；即在总共m+n-2步中选取m-1步
### 总步数C(m-1)(m+n-2) = (m+n-2)!/(m-1)!(n-1)!
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # math包下有阶乘函数factorial()，现手写递归实现
        def factorial(n):
            # 注意：0!=0
            if n==0:
                return 1
            else:
                return n * factorial(n-1)
        return factorial(m+n-2)//(factorial(m-1)*factorial(n-1))

### Solution3:动态规划，建立一个与地图等大的dp二维列表，初始化为1（避免单独讨论最左和最上边缘的情况）
### 其他部分dp[i][j]=dp[i-1][j]+dp[i][j-1]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n]*m
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
