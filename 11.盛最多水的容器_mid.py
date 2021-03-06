### content:
### 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
### 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
### 说明：你不能倾斜容器，且 n 的值至少为 2。

### solution:
### 暴力法：果然超时，我就不应该写出来
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # n = len(height)
        # most = 0
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         most = max(most, min(height[i],height[j])*(j-i))
        # return most
        
### 双指针收缩法：左右两个指针按照特定规则向内收缩直至相遇
### 特定规则：短板向内收缩（若长板收缩盛水量只能变小），等长向内同缩
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j,most = 0,len(height)-1,0
        while i<j:
            # most = max(most, min(height[i],height[j])*(j-i))
            if height[i]<height[j]:
                most = max(most, height[i]*(j-i))
                i += 1
            elif height[i]==height[j]:
                most = max(most, height[i]*(j-i))
                i += 1
                j -= 1
            else:
                most = max(most, height[j]*(j-i))
                j -= 1
        return most
        
