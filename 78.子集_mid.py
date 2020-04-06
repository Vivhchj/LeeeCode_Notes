# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。

# 示例:
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


### Solution1: 顺序加合法
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 结果集列表，默认有一个空[]
        res = [[]]
        # 将nums中的数字逐个加入res
        for num in nums:
            # 每个num都加到当前所有结果集的所有子列表中，例如[]+[3]=>[3]，[1,3]+[4]=>[1,3,4]
            temp = []
            for b in res:
                temp.append(b+[num])
            # 将当前num的所有加合集temp加入res
            res.extend(temp)
        return res
		
### Solution2: 顺序加合法plus
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 结果集列表，默认有一个空[]
        res = [[]]
        # 将nums中的数字逐个加入res
        for num in nums:
            # 每个num都加到当前所有结果集的所有子列表中，例如[]+[3]=>[3]，[1,3]+[4]=>[1,3,4]
			# 将加合结果加入res
			# 此种写法一行更比三行强
            res += [curr+[num] for curr in res]
        return res
