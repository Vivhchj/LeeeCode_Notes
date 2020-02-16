# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

# 示例:
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6

### Solution1:动态规划(Dynamic Programming,DP)：大事化小，将待解决的问题分成若干重复的小问题。
### 左右遍历一遍分别生成每个索引位置左边最高和右边最高的数组left_max[]和right_max[]，最后再来一遍遍历
### 最后一遍的遍历结合left_max[]和right_lmax[]，求出当前位置接的雨水高度 
class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        # height[]长度小于2的直接返回0
        if length<=2: 
            return 0
        # 定义left_max[]和right_max[]
        left_max, right_max = [0]*length, [0]*length
        left_max[0], right_max[-1] = height[0], height[-1]
        # 第一遍遍历，完善left_max[]和right_max[]
        for i in range(1, length):
            left_max[i] = height[i] if left_max[i-1] < height[i] else left_max[i-1]
            right_max[length-1-i] = height[length-1-i] if height[length-1-i] > right_max[length-i] else right_max[length-i]
        # 第二遍遍历，计算每个索引位置应接的雨水
        result = 0
        for i in range(1, length-1):
            if left_max[i] >= height[i] and right_max[i] >= height[i]:
                result += min(left_max[i], right_max[i]) - height[i]
        return result

### Solution2:双指针法：左右两侧分别一个指针表示目前检索到的最大高度
### 指针移动方式：当left_max<=right_max时，左指针右移一步，否则左移一步；
### 每次移动一步就使用二者中较小值与当前索引位置的高度来判断是否可以接水，作差即可得到当前索引位置所接的雨水量
class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        # height[]长度小于2的直接返回0
        if length<=2: 
            return 0
        # 定义双指针left和right
        left, right = 0, length-1
        # 定义左右遍历的最高高度
        left_max, right_max = height[0], height[length-1]
        # 一遍遍历
        result = 0
        while left < right:
            if left_max <= right_max:
                left += 1
                if height[left] < left_max:
                    result += left_max - height[left]
                else:
                    left_max = height[left]
            else:
                right -= 1
                if height[right] < right_max:
                    result += right_max - height[right]
                else:
                    right_max = height[right]
        return result

