###content:
###给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
###示例 1：
###输入: "babad"
###输出: "bab"
###注意: "aba" 也是一个有效答案。
###示例 2：
###输入: "cbbd"
###输出: "bb"

###solution:
###1.动态规划法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length<2:
            return s
        # 建二维数组dp[i][j]用于存储字段回文性质,初始化为0
        dp = [[0 if i!=j else 1 for i in range(length)]for j in range(length)]
        maxlen = 1
        # 返回值初始化为s[0],即为当没有回文子串出现时的答案
        result = s[0]
        # 动态规划结构，判断向右扩展一位后有没有新的或更长的回文子串出现
        for i in range(1, length):
            # 判断位置j到i组成的字串是否回文
            for j in range(i):
                if s[i]==s[j] and (dp[j+1][i-1] or i-j<=2):
                    dp[j][i] = 1
                    cur_len = i-j+1
                    if cur_len>maxlen:
                        maxlen = cur_len
                        result = s[j:i+1]
        return result

###2.中心扩展法
class Solution:
    def longestPalindrome(self, s: str) -> str:        
        length = len(s)
        maxlen = 0
        result = ""
        for i in range(length):
            # 求以每个位置i或(i,j)为起点所能扩展的最长回文子串
            len1 = s_extend(s, i, i)
            len2 = s_extend(s, i, i+1)
            if len1>len2 and (2*len1-1)>maxlen:
                result = s[i-len1+1 : i+len1]
                maxlen = 2*len1-1
            elif len2>=len1 and 2*len2>maxlen:
                result = s[i-len2+1 : i+len2+1]
                maxlen = 2*len2
        return result
    
def s_extend(s: str, start: int, end: int) -> int:
    length = len(s)
    l = 0
    while start>=0 and end<length:
        if s[start]==s[end]:
            l += 1
            start -= 1
            end += 1
        else:
            break
    return l

###3.manacher算法：字符间添加相同符号如#使得奇偶情况都变为奇数情况，另首位添加同样符号#或其他标识符如^&均可；
### 记录一个最右扩展点r_max和对应的中心点mid,每次对目标点right进行扩散时判断其是否在r_max内，
### 在其中的话则与中心对称点相对称的左边一个点left在r_max范围内对称，若left的扩展值在mid扩展半径内（r_max-mid）,则直接用left的值即可，省去了这部分的计算时间，
### 若超出则用r_max-right,超出r_max的需再用中心扩展法，并更新r_max和mid
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 排除特殊情况干扰
        if len(s)<2:
            return s
        # "*".join(string)函数用于指定字符*连接序列中元素后生成的新字符串；也常用于将非字符串序列变为字符串，如"".join(s)
        s1 = '$#'+'#'.join(s)+'#@'
        r_max = 0  #已遍历的最大右边界
        mid = 0  #对应的中心点
        l = len(s1)
        # 初始化一维数组(列表list)方法
        dp = [0]*l
        for i in range(1,l-1):
            # 利用之前保存的值
            if i<r_max:
                # 不能超过已遍历的右边界
                dp[i] = min(r_max-i,dp[mid+ mid-i])
            t = 0
            # 继续扩张
            while 1:
                if s1[i+dp[i]+t]!=s1[i-dp[i]-t]:
                    break
                t+=1
            dp[i]+=t-1
            # 更新边界值
            if i+dp[i]>r_max:
                r_max = i+dp[i]
                mid = i
        maxlen,maxidx = 0,0
        # 找到最大子串
        # 调用现有函数居然用时更长……（92ms->100ms）
        # maxlen = max(dp)
        # maxidx = dp.index(maxlen)
        for i in range(l):
            if dp[i]>maxlen:
                maxlen = dp[i]
                maxidx = i
        return s1[maxidx-maxlen:maxidx+maxlen+1].replace('#',"")
