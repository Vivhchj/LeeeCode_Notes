### content:
### 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
### 有效字符串需满足：
###  左括号必须用相同类型的右括号闭合。
###  左括号必须以正确的顺序闭合。
###  注意空字符串可被认为是有效字符串。

### 示例 :
### 输入: "()[]{}"
### 输出: true

### solution1: 利用栈的思想，未配对（左括号）则进栈，遇到右括号，若配对则出栈，否则判错
class Solution:
    def isValid(self, s: str) -> bool:
        ## 专门用于判断是否配对的
        judge = ['()','[]','{}']

        left = ['(','[','{']
        l,j = [],-1
        for i in s:
            ## 如果是左括号则进栈
            if i in left:
                l.append(i)
                j += 1
            ## 右括号则进行匹配判断
            else:
                if l:
                    l[j] += i
                    if l[j] in judge:
                        l.pop()
                        j -= 1
                    else:
                        break
                else:
                    j += 1
                    break
        return True if j==-1 else False

# ### solution2: 同样是栈的思想，你的解答为何如此优秀
class Solution:
    def isValid(self, s: str) -> bool:
        # The stack to keep track of opening brackets.
        stack = []
        ## 用字典来查找和判断（better than my above list）
        mapping = {")": "(", "}": "{", "]": "["}
        # For every bracket in the expression.
        for char in s:
            # If the character is an closing bracket（右括号）
            ## "if key in dict: ……"用于判断键是否在字典中
            if char in mapping:
                ## 当遇到右括号时，直接令栈（列表）的最后一个元素出栈，
                # list.pop()默认移除列表的最后一个元素并返回该值
                top_element = stack.pop() if stack else '#'
                ## 判断是否配对
                if mapping[char] != top_element:
                    return False
            else:
                ## opening bracket（左括号）, simply push it onto the stack.
                stack.append(char)
        return not stack
