# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

# 必须原地修改，只允许使用额外常数空间。

# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 3,6,5,3,2 → 5,2,3,3,6

### Solution:
# 判断从末位往前组成的数是不是最大，不是的话改成最大（由大到小顺序）
# 判断当前组合的数字，首位a是否最大（即由大到小顺序），不是的话就改
# 改动规则：把当前位改成比之前大的最小的数字，剩下的按由小到大顺序排列
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        L = len(nums)
        max_num, flag = 0, 0
        for i in range(L):
            # 判断改动
            if nums[L-i-1] < max_num:
                flag = 1
                # 找到新首位
                for j in range(i):
                    if nums[L-j-1] > nums[L-i-1]:
                        # python里居然可以这么写列表翻转
                        nums[L-i-1], nums[L-j-1] = nums[L-j-1], nums[L-i-1]
                        # temp = nums[L-i-1]
                        # nums[L-i-1] = nums[L-j-1]
                        # nums[L-j-1] = temp
                        break
                # 此时，nums[L-i:]仍然是降序的，只需要将其翻转为升序即可
                j = 0
                while L-i+j < L-1-j:
                    nums[L-1-j], nums[L-i+j] = nums[L-i+j], nums[L-1-j]
                    # temp = nums[L-1-j]
                    # nums[L-1-j] = nums[L-i+j]
                    # nums[L-i+j] = temp
                    j += 1
                break
            else:
                max_num = nums[L-i-1]
        if flag==0:
            nums.sort()
