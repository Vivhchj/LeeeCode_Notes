### content:
### 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

### 示例：
### 输入：给定数组 nums = [-1，2，1，-4], target = 1.
### 输出：2
### 解释：与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

### solution:
### 基本思路与上一题求三数之和相同，双指针扫描
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        if n<3: return 0
        flag = 1000
        result = 0
        for i in range(n-2):
            j,k = i+1,n-1
            if i>0 and nums[i-1]==nums[i]: continue
            while j<k:
                ## 判断区域内最大值是否小于target，或最小值是否大于target
                ## 成立则稍做判断(是否是当前最优解)后退出循环，否则利用双指针进行扫描
                min_sum = nums[i]+nums[j]+nums[j+1]
                max_sum = nums[i]+nums[k]+nums[k-1]
                if min_sum > target:
                    diff = min_sum - target
                    if diff < flag:
                        flag,result = diff,min_sum 
                    break
                elif max_sum < target:
                    diff = target - max_sum
                    if diff < flag:
                        flag,result = diff,max_sum
                    break
                else:
                    ## 正常双指针扫描
                    summ = nums[i]+nums[j]+nums[k]
                    diff = abs(target-summ)
                    if diff < flag:
                        flag,result = diff,summ 
                    ## 指针移动，且跳过重复值
                    if summ < target:
                        j += 1
                        while j<k and nums[j]==nums[j-1]: j += 1
                    elif summ > target:
                        k -= 1
                        while j<k and nums[k]==nums[k+1]: k -= 1
                    else:
                        return target
        return result
