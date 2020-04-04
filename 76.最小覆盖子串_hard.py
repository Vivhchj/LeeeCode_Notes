# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

# 示例：
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
# 说明：

# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。


### Solution1: 从头暴力匹配(最后一个用例超时)
### 对于每个遍历到的目标字符，从该处开始往后遍历指定长度（已知最短有效字串长度或到末尾的长度），寻找目标字符串
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length = len(s)
        min_idx, min_len, r_p = -1, length, length-len(t)
        # 从头开始遍历
        for i in range(r_p+1):
            # 若此索引处元素包含于t中，于此开始往下遍历max_len长度以内，看有没有更短的符合子串
            if s[i] in t:
                # temp用于存储当前已遍历到的目标字符
                temp = list(t)
                for j in range(0, min(min_len, length-i)):
                    if s[i+j] in temp:
                        temp.remove(s[i+j])
                        if not temp:
                            min_idx, min_len = i, j+1
                            break
        if min_idx != -1:
            return s[min_idx : (min_idx+min_len)]
        else:
            return ""

### Solution2: 滑动窗口（双指针移动，loop:（先移动r得到一个匹配，再移动l得到最小匹配））
### 使用Counter类型进行计数
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s=="" or t=="":
            return ""
        t = Counter(t)
        l, r = 0, 0
        min_idx, min_len = -1, len(s)+1
        # temp用于存储当前遍历字符串的情况（字符与个数统计）
        temp = Counter()
        # 从头开始遍历，直至r指针指向最末尾元素
        # 首先l不动，r右移
        while r < len(s):
            # 更新——增加
            temp.update(s[r])
            # 如果当前字符串符合要求，r不动，l右移至最优（短）字符串
            if not list(t-temp):
                # 得到当前字符串的最优字符串
                while not list(t-temp):
                    # 更新——减少
                    temp.subtract(s[l])
                    l += 1
                # 如若是最短字符串，记录
                if r-l+2 < min_len:
                    min_len = r - l + 2
                    min_idx = l - 1
            r += 1
        if min_idx != -1:
            return s[min_idx : (min_idx+min_len)]
        else:
            return ""

### Solution3: 优化滑动窗口，去除s中t没有的字符（双指针移动，loop:（先移动r得到一个匹配，再移动l得到最小匹配））
### 使用Counter类型进行计数，
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s=="" or t=="":
            return ""
        s_lite = []
        for idx, s_i in enumerate(s):
            if s_i in t:
                s_lite.append((idx, s_i))
        t = Counter(t)
        l, r = 0, 0
        min_idx, min_len = -1, len(s)+1
        # temp用于存储当前遍历字符串的情况（字符与个数统计）
        temp = Counter()
        # 从头开始遍历，直至r指针指向最末尾元素
        # 首先l不动，r右移
        while r < len(s_lite):
            # 更新——增加
            temp.update(s_lite[r][1])
            # 如果当前字符串符合要求，r不动，l右移至最优（短）字符串
            if not list(t-temp):
                # 得到当前字符串的最优字符串
                while not list(t-temp):
                    # 更新——减少
                    temp.subtract(s_lite[l][1])
                    l += 1
                # 如若是最短字符串，记录
                if s_lite[r][0]-s_lite[l-1][0]+1 < min_len:
                    min_len = s_lite[r][0]-s_lite[l-1][0]+1
                    min_idx = s_lite[l-1][0]
            r += 1
        if min_idx != -1:
            return s[min_idx : (min_idx+min_len)]
        else:
            return ""

### Solution4: 进一步优化滑动窗口，随着right移动每次判断最优的[left, right]范围，再移动right找到从left+1开始的匹配子串
### defaultdict类型不同模式代表不同value类型，value为默认初始化值
### int模式可进行计数，key不论有无默认value均为0
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mem = defaultdict(int)
        for char in t:
        	mem[char]+=1
        t_len = len(t)

        minLeft, minRight = 0, len(s)
        left = 0
		# 右指针从头移动到尾
        for right,char in enumerate(s):
        	if mem[char]>0:
        		t_len-=1
        	mem[char]-=1
			# 得到目标字符串，范围[l, r]
        	if t_len==0:
				# 关键部分
				# l后移至最短子串左端点，对于t中没有的字符，mem[]一定<0;
				# 移动到mem[]=0的位置，此处字符s[left]等于t中个数，即它是首个个数最优的字符
        		while mem[s[left]]<0:
        			mem[s[left]]+=1
        			left+=1
				# 更新最短字符串
        		if right-left<minRight-minLeft:
        			minLeft,minRight = left,right
				
				# left后移，当前字符串不再是匹配字符串，缺少一个字符s[left-1]，故t_len要加1
        		mem[s[left]]+=1
        		left+=1
				t_len+=1
				# 一次loop结束，移动右指针寻找下一个匹配字符串
        return '' if minRight==len(s) else s[minLeft:minRight+1]
