# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。

# 示例 1：
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶

# 示例 2：
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶

### Solution1：数学规律，对每种情况下爬1阶2阶的次数进行排列组合
class Solution:
    def climbStairs(self, n: int) -> int:
        # 自写阶乘函数
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)

        result = 0
        # i表示爬二阶楼梯的次数
        for i in range(n//2 + 1):
            # 
            m = n - 2*i
            # 每种情况的方案数公式C(m)(m+i)=(m+i)!/(m!*i!)
            result += factorial(m+i)//(factorial(m)*factorial(i))
        return result

### Solution2：规律，f(n)=f(n-1)+f(n-2)，
### 即f(n)可分为(n-1)+1，以及(n-2)+2两种情况（(n-2)+1+1的情况包含在前者当中）
### 递归写会超时，采用动态规划写
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1]*(n+1)
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        # # dp[]列表改为两个变量
        # former, latter = 1, 1
        # for i in range(n//2):
        #     former += latter
        #     latter += former
        # return latter if n%2 else former
        
