### 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
### 返回被除数 dividend 除以除数 divisor 得到的商。

### 示例 1:
### 输入: dividend = 10, divisor = 3
### 输出: 3

### 示例 2:
### 输入: dividend = 7, divisor = -3
### 输出: -2

### 说明:
### 被除数和除数均为 32 位有符号整数。除数不为 0。
### 假设我们的环境只能存储 32 位有符号整数，其数值范围是[−2^31, 2^31 − 1]。本题中，如果除法结果溢出，则返回2^31 − 1。

### Solution:传统除法转减法思想的进化版，递归思想，减数（除数）层层加倍（这里加倍采用位运算），直至不能再加倍，再回溯。
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 负数表示范围较大，采用负数进行计算
        if dividend>0:
            sign1 = 1
            dividend = -dividend
        else:
            sign1 = -1
        if divisor>0:
            sign2 = 1
            divisor = -divisor
        else:
            sign2 = -1

        ## 商，为防止正数溢出，先用负数表示
        quot = 0
        def divd(dividend: int, divisor: int, time: int) -> int:
            ## nonlocal语句只能在被嵌套函数内部进行使用
            nonlocal quot 
            ## 进到递归里，判断是否能正向（减数递增）减，可以的话减完进入下一层递归，否则返回上一层
            if dividend <= divisor:
                dividend -= divisor
                quot -= time
                ## 使用位运算符加速计算，'<<n'表示乘2的n次方
                dividend = divd(dividend, divisor<<1, time<<1)
                ## 返回后判断能否反向（减数递减）减，不论是否可以，减完都回到上一层
                if dividend <= divisor:
                    dividend -= divisor
                    quot -= time
                return dividend
            else:
                return dividend
        
        divd(dividend, divisor, 1)
        
        ## 对于商为正数的情况，先判断是否是INT_MIN，再改成正数
        if sign1+sign2!=0:
            if quot==-2147483648:
                quot = 2147483647
            else:
                quot = -quot
        return quot
