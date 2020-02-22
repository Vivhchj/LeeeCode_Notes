# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例:
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

### Solution1：遍历一次，求得以每一个位置为终点的连续子数组的最大值
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = nums[0]
        for i in range(1, len(nums)):
            # 遍历过的nums[i]记录每个位置为终点的的最大子序和
            nums[i] = max(nums[i-1], 0) + nums[i]
            # max_value更新遍历到的最大子序和
            max_value = max(nums[i], max_value)                 
        return max_value

### Solution2：分治法，递归地将数组一分为二，求解时分别求左边、右边，以及中间三部分
### 左边和右边都是取所划分的三部分的最大值，中间部分则要从中点开始分别往前和往后遍历完数组并取最大累加值之和
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 函数用于求从start开始（必须包含start点）到stop中的最大子序和，正序还是反序由sign的正负决定
        def mid_cal(start, stop, sign) -> int:
            # 只有一个点，直接返回该点
            if start==stop: 
                return nums[start]
            else:
                value, max_value = 0, float('-inf')
                for i in range(start, stop, sign):
                    # value表示从start到当前位置的子序和（累加和）
                    value += nums[i]
                    # max_value表示目前最大累加和
                    max_value = max(max_value, value)
            return max_value

        # 传入参数：左右索引；返回最大子序和
        def half_div(left: int, right: int) -> int:
            # 一直二分到只有一个元素
            if left==right:
                return nums[left]
            else:
                # 中间点索引
                mid_idx = (left+right)//2
                # 求左边和右边的最大子序和
                max_left = half_div(left, mid_idx)
                max_right = half_div(mid_idx+1, right)
                # 求一定包含中间点的最大子序和
                # 先求左半部分，由中间点到左端点
                mid_left = mid_cal(mid_idx, left-1, -1)
                # 后求右半部分，由中间点+1的位置到右端点
                mid_right = mid_cal(mid_idx+1, right+1, 1)
                # 两部分之和
                max_mid = mid_left + mid_right
            return max(max_left, max_right, max_mid)
        
        return half_div(0, len(nums)-1)
