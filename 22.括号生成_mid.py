### content:
### 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

### 示例：输入n = 3
### 输出：
### [
###   "((()))",
###   "(()())",
###   "(())()",
###   "()(())",
###   "()()()"
### ]


### solution1:我的笨笨的递归
### 利用栈的状态来判断是否还有(和)可以组合
### 若仍有未使用(，（m>=1），则必有(可以入栈；若栈不为空，必有)可以组合；
### 若(用完，则将剩余的)全部加到末尾
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def gnrt(stack: str, string: str, m: int):
            if m>=1:
                gnrt(stack+"(", string+"(", m-1)
                if len(stack):
                    gnrt(stack[:-1], string+")", m)
            else:
                result.append(string+")"*len(stack))
        
        gnrt("", "", n)
        return result

### solution2:官方题解，不做人的回溯法
class Solution:
    # # 此函数的作用是返回N组括号的所有组合
    def generateParenthesis(self, n: int) -> List[str]:
        # 长度为0，返回''
        if n == 0: return ['']
        ans = []
        # 生成所有n组括号的组合,left和right进行全排列
        for c in range(n):
            # 所有left组合
            for left in self.generateParenthesis(c):
                # 所有right组合
                for right in self.generateParenthesis(n-1-c):
                    # 格式化字符串的函数str.format()，可以接受不限个参数，顺序可以自己规定，默认前后顺序。
                    # str中的每个{}对应后面的参数，此处为'({left}){right}'
                    ans.append('({}){}'.format(left, right))
        return ans

### solution3:动态归划
### 从0～n，逐渐生成到n组的括号。同样通过'({left}){right}'的形式，生成n组括号时，left+right有(0,n-1)…(i,n-1-i)…(n-1,0)共n-1种情况。
### 
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        # 0组括号时记为""，1组括号只有"()"一种情况
        total_l = [[""], ["()"]]
        for i in range(2,n+1):    # 开始计算i组括号时的括号组合
            l = []
            # 开始遍历 p q ，其中p+q=i-1 , j 作为索引
            for j in range(i):
                # p = j 时的括号组合情况
                now_list1 = total_l[j]
                # q = (i-1) - j 时的括号组合情况
                now_list2 = total_l[i-1-j]    
                # 两部分排列组合
                for k1 in now_list1:  
                    for k2 in now_list2:
                        el = "(" + k1 + ")" + k2
                        l.append(el)    # 把所有可能的情况添加到 l 中
            total_l.append(l)    # l这个list就是i组括号的所有情况，添加到total_l中，继续求解i=i+1的情况
        return total_l[n]
