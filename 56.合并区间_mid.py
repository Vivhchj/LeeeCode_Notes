# 给出一个区间的集合，请合并所有重叠的区间。

# 示例 1:
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

# 示例 2:
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

### Solution1:排序法
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 升序排序
        intervals.sort()
        i = 0
        # 遍历列表，如果下一个区间i+1与当前区间i重叠，则在i上合并两个区间并pop(i+1)；否则进入下一个区间i+1
        while i < len(intervals)-1:
            if intervals[i][1]>=intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals[i][0] = min(intervals[i][0], intervals[i+1][0])
                intervals.pop(i+1)
            else:
                i += 1
        return intervals
