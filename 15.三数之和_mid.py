### content:
### 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
### 注意：答案中不可以包含重复的三元组。

### 示例：
### 输入：nums = [-1, 0, 1, 2, -1, -4]，
### 输出：[[-1, 0, 1],[-1, -1, 2]]

### solution:
### 思路：首位固定+双指针向中移动
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        i = 0
        for i in range(n-2):
            ## 临界条件：固定点i（最小加数）大于0后和一定不为0
            if nums[i]>0: break
            ## 跳过固定点的值重复的情况
            if i>0 and nums[i]==nums[i-1]: continue
            ## 双指针
            j,k = i+1,n-1
            while k > j:
                # ## 加上这句话居然耗时更长 
                # if nums[k]<0: break
                num = nums[i]+nums[j]+nums[k]
                if num > 0:
                    ## 当和大于0时，需要k左移使和减小
                    k -= 1
                    while nums[k+1]==nums[k] and k>j: k -= 1
                elif num < 0:
                    ## 当和小于0时，需要j右移使和增大
                    j += 1
                    while nums[j-1]==nums[j] and j<k: j += 1
                else:
                    result.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while nums[j-1]==nums[j] and j<k: j += 1
                    k -= 1
                    while nums[k+1]==nums[k] and k>j: k -= 1
        return result
        
 ### 引申到通用N数字加和的函数
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        ## N个数相加和为target求加数的通用函数，一步步拆分成两两相加的情况
        def findNsum(nums, target, N, result):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                l,r = 0,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(len(nums)-N+1):
                    if i == 0 or nums[i-1] != nums[i]:
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]])

        ## 调用时记得先将列表排序
        findNsum(sorted(nums), 0, 3, [])
        return results
    
