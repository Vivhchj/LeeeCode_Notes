###content:给出一个 32 位的有符号整数，需要将这个整数中每位上的数字进行反转。
###假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。如果反转后整数溢出那么就返回 0。
###示例 1:
###输入: -123
###输出: -321

###solution:
###1.整数转换成字符串进行操作，再转回来，不推荐
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        # 若输入数字x为空或个位则直接输出
        if len(s)<2:
            return x
        if s[0]=='-':
            flag = -1
            s = s[1:]
        else:
            flag = 1
        # 去除末尾（两端）的0
        s = s.strip('0')
        # 字符串反转
        s = flag * int(s[::-1])
        if s<-1*pow(2,31) or s>pow(2,31)-1:
            s = 0
        return s


###2.循环pop和push操作（剥离x的个位数加到result上）
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = pow(2,31)-1  # 2147483647
        # 注意：python负数运算区别于其他，需要先将负数变为正数；如果用C++或java则没有此问题。
        flag = 1 if x>=0 else -1
        # 取绝对值
        x, result = abs(x), 0
        while x:
            # 剥离个位数
            pop = x % 10
            x //= 10
            # 正数越界判断
            if flag==1 and (result>INT_MAX//10 or (result==INT_MAX//10 and pop>7)):
                return 0
            # 负数越界判断
            if flag==-1 and (result>INT_MAX//10 or (result==INT_MAX//10 and pop>8)):
                return 0
            result = result*10 + pop
        return result*flag
