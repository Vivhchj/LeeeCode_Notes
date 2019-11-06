### content:
### 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
### 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

### 示例:
### 给定 nums = [0,0,1,1,1,2,2,3,3,4],
### 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
### 你不需要考虑数组中超出新长度后面的元素。

### solution1:最初级的思路：正向遍历并删除重复数组，因为索引会变化，所以要用while对索引和数组长度进行动态调整
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1
        while i<n:
            if nums[i]==nums[i-1]:
                nums.pop(i)
                n -= 1
            else:
                i += 1
        return n

### solution2:初级思路：反向遍历并删除重复数组，索引不会变化
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # range()函数用法：range(stop), range(start, stop[, step])，取值范围左闭右开[start, stop)
        for i in range(len(nums)-1, 0, -1): # step=-1，意为倒序，由大到小，此时start>stop
            if nums[i]==nums[i-1]:
                nums.pop(i)
        return len(nums)

### solution3: 不进行删除操作，将前面的值替换成不重复的，不管后面多余的部分（强烈不推荐）
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        # 从头遍历数组nums
        for i in range(len(nums)-1):
            # 如果不相等，计数+1
            if nums[i]!=nums[i+1]:
                nums[count] = nums[i+1]
                count += 1
        return count

