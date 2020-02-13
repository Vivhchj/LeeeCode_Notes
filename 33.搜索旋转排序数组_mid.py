# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 你可以假设数组中不存在重复的元素。
# 你的算法时间复杂度必须是 O(log n) 级别。

# 示例 1:
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4

# 示例 2:
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1

### Solution:二分法
### 1.函数递归
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 每次将一个大区间分成两个小区间，即必有一个升序区间，另一个可能恰好是升序也可能不是
        # 对于升序区间，用 '首位<=target' and 'target<=末位' 判断；升降区间
        # 一直到区间只剩一项
        def half_div(min_idx: int, max_idx: int, length: int) -> int:
            # print(min_idx, max_idx, length)
            if length>1 and (nums[min_idx] <= target or target <= nums[max_idx]):
                half_idx = min_idx + (length-1)//2
                # 根据四种不同情况取特定区间
                if nums[min_idx] <= nums[half_idx]:
                    # 1.前半升序且存在target
                    if nums[min_idx] <= target <= nums[half_idx]:
                        max_idx = half_idx
                    # 2.前半升序而target在后半区间
                    else:
                        min_idx = half_idx + 1
                else:
                    # 3.后半升序且存在target
                    if nums[half_idx+1] <= target <= nums[max_idx]:
                        min_idx = half_idx + 1
                    # 4.后半升序而target在前半区间
                    else:
                        max_idx = half_idx
                return half_div(min_idx, max_idx, max_idx-min_idx+1)
            # 二分到区间只有一项时判断此项是否是target
            elif length==1 and nums[min_idx]==target:
                return min_idx
            else:
                return -1

        # 传递索引
        length = len(nums)
        max_idx = length - 1
        min_idx = 0
        return half_div(min_idx, max_idx, length)
### 2.将函数递归改为循环
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 每次将一个大区间分成两个小区间，即必有一个升序区间，另一个可能恰好是升序也可能不是
        # 对于升序区间，用 '首位<=target' and 'target<=末位' 判断；升降区间
        # 一直到区间只剩一项
        result = -1
        # 定义区间长度和区间左右界（索引）
        length = len(nums)
        left, right = 0, length-1
        # 当区间内大于一项时，进行区间二分
        while length > 1:
            half = left+(length-1)//2
            # 当区间是升序区间时，根据target与nums[half]的关系留下所在区间
            if nums[left] < nums[right]:
                if nums[half] >= target:
                    right = half
                else:
                    left = half + 1
            # 当区间是升降区间时，
            else:
                # 如果左区间是升序区间
                if nums[left] <= nums[half]:
                    if nums[left] <= target <= nums[half]:
                        right = half
                    else:
                        left = half + 1
                # 如果右区间是升序区间
                else:
                    if nums[half+1] <= target <= nums[right]:
                        left = half + 1
                    else:
                        right = half
            length = right-left+1
            # print(length, left, right)
        if length == 1 and nums[left]==target:
            result = left
        else: 
            pass
        return result
        
