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
