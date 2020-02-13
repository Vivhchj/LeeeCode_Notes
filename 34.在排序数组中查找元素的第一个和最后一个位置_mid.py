# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 你的算法时间复杂度必须是 O(log n) 级别。
# 如果数组中不存在目标值，返回 [-1, -1]。

# 示例 1:
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]

# 示例 2:
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]

### Solution:二分法
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        length = len(nums)
        left, right, half = 0, length-1, (length-1)//2
        # 寻找左端点
        while left < right:
            # 找到target的最小索引（只要左侧有，不论右侧有没有，都检索左区间）
            if nums[half] >= target:
                right = half
            else:
                left = half + 1
            length = right - left + 1
            half = left + (length - 1) // 2
        # 若找到左端点，则找右端点
        if length==1 and nums[left]==target:
            result[0] = left
            right = len(nums) - 1
            length = right - left + 1
            half = left + length//2
            while left < right:
                # 只要右侧有，就检索右侧
                if nums[half] <= target:
                    left = half
                else:
                    right = half-1
                length = right - left + 1
                half = left + length//2
            result[1] = left
        # 若找不到左端点则记为不存在
        else:
            pass
        return result
