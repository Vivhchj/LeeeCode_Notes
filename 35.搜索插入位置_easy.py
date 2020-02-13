# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 假设数组中无重复元素。

# 示例 1:
# 输入: [1,3,5,6], 5
# 输出: 2

# 示例 2:
# 输入: [1,3,5,6], 2
# 输出: 1

# 示例 3:
# 输入: [1,3,5,6], 7
# 输出: 4

# 示例 4:
# 输入: [1,3,5,6], 0
# 输出: 0

### Solution: 二分法
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        result = -1
        length = len(nums)
        left, right, half = 0, length-1, length//2
        while left <= right:
            # 当target比区间左端点还小或者在左端点上时，一定会在left位置
            if target <= nums[left]:
                result = left
                break
            # 当target比区间右端点还大时，一定会在right+1位置
            elif target > nums[right]:
                result = right + 1
                break
            # 当target在左区间中，取左区间
            elif nums[left] < target < nums[half]:
                right = half - 1
            # 当target在右区间，取右区间
            else:
                left = half
            length = right - left + 1
            half = left + length // 2
        return result
