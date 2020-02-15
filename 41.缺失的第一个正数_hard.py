# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

# 示例 1:
# 输入: [1,2,0]

# 输出: 3
# 示例 2:
# 输入: [3,4,-1,1]
# 输出: 2

# 示例 3:
# 输入: [7,8,9,11,12]
# 输出: 1

# 说明:你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。

### Solution:一个萝卜一个坑的思想，把合理范围内的正数[1,n]放到自己该有的位置上
### 首先遍历第一遍数组，一个萝卜一个坑的思想，将[1,n]范围内的正数i放到nums[i-1]处
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        result = n + 1
        for i in range(n):
            # 如果nums[i]在[1,n]范围内，且不处于正确位置，且要替换到的目标位置也不是正确位置，则一直循环替换
            # 也就是说，除了会将正确位置归位外，也会将不正确的或重复的留下；总之不会落下一个正确的无家可归
            while 1 <= nums[i] <= n and nums[i] != i+1 and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(n):
            if nums[i] != i+1:
                result = i + 1
                break
        return result
