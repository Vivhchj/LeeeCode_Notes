# 给定一个没有重复数字的序列，返回其所有可能的全排列。
# 示例:
# 输入: [1,2,3]
# 输出:
# [
  # [1,2,3],
  # [1,3,2],
  # [2,1,3],
  # [2,3,1],
  # [3,1,2],
  # [3,2,1]
# ]

### Solution:回溯法
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def arrange(sign):
            if sign==length:
                # 此处如果填nums，表示将nums的内存地址存入result，即单纯的引用，最终会导致result中的是全部一样的list；
                # 而nums[:]相当于使用复制函数nums.copy()，新建一个内存地址，与原来的nums[]没有任何交集
                result.append(nums[:])
            for i in range(sign, length):
                # 先将两个位置的值对换，使排列的值全部在sign前，未排列的值全部在sign后；
                nums[sign], nums[i] = nums[i], nums[sign]
                arrange(sign+1)
                # 上个排列用完之后再将对换的值换回原处
                nums[sign], nums[i] = nums[i], nums[sign]

        length = len(nums)
        if length > 1:
            arrange(0)
        else:
            result.append(nums)
        return result
