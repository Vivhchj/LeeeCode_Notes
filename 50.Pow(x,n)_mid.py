# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。

# 示例 1:
# 输入: 2.00000, 10
# 输出: 1024.00000

# 示例 2:
# 输入: 2.10000, 3
# 输出: 9.26100

# Solution1：递归法1——先由小到大，再由大到小
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0: 
            return 1
        elif x==0: 
            return 0
        # 负数次幂将x转成分数
        if n < 0:
            x = 1.0 / x
        # 为防止次幂数n溢出，采用负数计数
        else:
            n = -n

        result = x
        # 首先正向深入，i不断加倍，直至过半后回溯；传入参数是当前负的次幂数i，以及temp=x^(-i)；返回值是负的次幂数
        def powed(i, temp):
            # 内层嵌套函数调用外层变量要用nonlocal
            nonlocal result
            # pyhton整除是真 向下取整，因此整除不断时商要+1
            flag = n//2+1 if n%2 else n//2
            # 当i未过半时，按加倍进行运算，即自己乘自己——temp^2
            if i >= flag:
                result *= temp
                sign = powed(2*i, result)
            # i过半时，开始回溯
            else:
                return i
            # 回溯过程中，判断所剩次幂数是否大于等于当前i，是则乘入temp
            if i >= n-sign:
                result *= temp
                return i+sign
            else:
                return sign
        powed(-1, result)
        return result

### Solution2：递归法2——先由大到小，再由小到大；
### 思想：由大到小逐渐细分，确定要乘的元素但还不计算，再在回溯时由小到大将其累乘起来
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # python可以不考虑int型整数INT_MIN求负越界问题
        if n < 0:
            x =  1.0 / x
            n = -n
        # 递归函数，由大递归到小，回溯时进行运算，由小乘到大
        def Powed(x, n) -> float:
            # n==1代表递归最深处
            if n==1: return x
            # n==0既包含输入时n==0的特殊情况，也包含残差计算的一部分
            elif n==0: return 1
            # half表示成倍次幂
            half = Powed(x, n//2)
            # res(idual)表示half操作时是否会有残差（n//2的余数）
            res = Powed(x, n%2)
            return half*half*res
        
        return Powed(x, n)

### Solution3：二进制法
### 思想：n取正数后，二进制表示的每一位都代表是否需要乘，每一位代表的幂运算都是前一位的平方
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # python可以不考虑int型整数INT_MIN求负越界问题
        if n < 0:
            x =  1.0 / x
            n = -n
        result = 1
        while n:
            # 如果当前最末位是1（用按位与&运算可得）
            if n&1:
                result *= x
            # n后移一位，x也对应平方
            n >>= 1
            x *= x
        return result
