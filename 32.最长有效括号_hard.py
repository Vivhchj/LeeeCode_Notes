# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

# 示例 1:
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"

# 示例 2:
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"

### Solution:采用栈的思想，遍历一遍括号，遇到'('时记其索引，遇到')'时退出上一个'('的索引。
### 考虑')'过多的情况，用一个std表示前面的'('数，若前面无'('，则记下这个')'的索引。
### 即为，记下所有不能匹配的括号的索引，以及首尾的索引。其间最大间隔即为最长有效括号长度。
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        std, stack = 0, []
        for idx, si in enumerate(s):
            # 遇到'('记下索引（相当于将'('入栈）
            if si == '(':
                std += 1
                stack.append(idx)
            else:
            # 遇到')'根据匹配情况分别处理
                # 有效匹配，将与之匹配的'('（的索引）出栈
                if std>0:
                    std -= 1
                    stack.pop()
                # 无效括号，记下此')'的索引
                else:
                    stack.append(idx)
        max_l = 0
        # 如果中间有无效括号，则找到其中最大有效括号子串长度
        if len(stack):
            # 若s[0]是有效匹配，需要人为加入一个无效匹配索引[-1]
            if 0 in stack:
                pass
            else:
                stack.append(-1)
            # 若s[len(s)-1]是有效匹配，同样需要加入一个无效匹配索引[len(s)]
            if len(s)-1 in stack:
                pass
            else:
                stack.append(len(s))
            # 无效括号的索引升序排序
            stack.sort()
            # 根据各索引找到最大间隔
            for i in range(1,len(stack)):
                if stack[i]-stack[i-1]-1 > max_l:
                    max_l = stack[i]-stack[i-1]-1
                else:
                    pass
        # 如果s的所有括号全部匹配成功，则所求即为s长度
        else:
            max_l = len(s)
        return max_l


