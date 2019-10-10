### content:
### 编写一个函数来查找字符串数组中的最长公共前缀。
### 如果不存在公共前缀，返回空字符串 ""。
### 示例 1:
### 输入: ["flower","flow","flight"]
### 输出: "fl"

### solution:
### 1.大佬的巧妙方法：运用zip()函数和set()函数
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ## zip()函数将可迭代的对象作为参数，将对应的元素打包成一个个元组，返回由这些元组组成的对象。
        ## 即返回的对象中每个元素都是同一索引位置上的元素组成的元组，不等长时只取到共有的最大索引。
        ## 例：l = list(zip(["abcde","aef"]))  l为[('a','a'),('b','e'),('c','f')]
        ## set是一个不允许内容重复的组合，且set里的内容位置是无序的，不能用索引列出。
        ## 创建集合：可以使用大括号{}或者set()函数，
        ## 注意：创建一个空集合必须用set()而不是{}，因为{}用来创建一个空字典。
        ## 例：set(l[0]) = {'a'}, set(l[1])={'e','b'}(无序)
        result = ""
        for i in zip(*strs):
            if len(set(i))==1:
                result += i[0]
            else:
                break           
        return result

## 2.自己的暴力方法：找到最短的字串长度min_l，再判断每串的同一索引是否相同，直到不同或末尾
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n==0:
            return ""
        elif n==1:
            return strs[0]
        result = ""
        min_l = len(strs[0])
        ## 找到最小索引
        for i in strs:
            min_l = min(min_l, len(i))
        ## 暴力匹配
        for i in range(min_l):
            for j in range(n-1):
                if strs[j][i]==strs[j+1][i]:
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 0:
                break
            else:
                result += strs[0][i]
        return result
