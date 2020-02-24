# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。

# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

# 示例 1:
# 输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]

# 示例 2:
# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

### Solution1:使用python3的list.insert()和list.pop()函数，在所给列表中操作
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        # 遍历各个区间
        while i < len(intervals):
            # 如果当前区间在新区间左边，则遍历下一个
            if intervals[i][1] < newInterval[0]:
                i += 1
            # 如果当前区间在新区间右边，则将新区间插入到intervals的这个位置，结束操作
            elif intervals[i][0] > newInterval[1]:
                intervals.insert(i, newInterval)
                break
            # 如果当前区间i与新区间产生重叠，将新区间更新为与当前区间i的重叠区间，并将当前区间pop(i)掉
            # 下次循环判断下一个区间i,因为pop()操作，索引不必改变
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
                intervals.pop(i)
        # 如果所有区间都在新区间左边，则将新区间加到末尾即可
        if i == len(intervals):
            intervals.append(newInterval)
        return intervals

### Solution2：不使用两个列表插入删除元素函数的法1
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, result = 0, []
        while i < len(intervals):
            # 如果当前区间在新区间左边，直接将当前区间加到result中
            if intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            # 如果当前区间在新区间右边，将新区间以及当前区间开始的剩余区间都加到result中，结束
            elif intervals[i][0] > newInterval[1]:
                result += [newInterval] + intervals[i:]
                break
            # 否则当前区间与新区间重叠，合并两者到新区间
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        # 如果新区间一直大于列表的区间，那会遍历到列表末尾，i==len(intervals)，因此将新区间加到末尾
        if i == len(intervals):
            result.append(newInterval)
        return result

### Solution3:贪心算法，对这里的贪心不是很理解
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, n, result = 0, len(intervals), []
        # 每次列表区间在新区间左右边时，直接将其加入result
        while i < n and intervals[i][0] <= newInterval[0]:
            result.append(intervals[i])
            i += 1
        # 加入newInterval，先判断是否与result[-1]重叠
        if not result or newInterval[0] > result[-1][1]:
            result.append(newInterval)
        else:
            result[-1][0] = min(newInterval[0], result[-1][0])
            result[-1][1] = max(newInterval[1], result[-1][1])
        # 后续每个区间都要与上一个比较，如有重叠则更新
        while i < n and result[-1][1] >= intervals[i][0]:
            result[-1][0] = min(result[-1][0], intervals[i][0])
            result[-1][1] = max(result[-1][1], intervals[i][1])
            i += 1
        # 重叠部分更新完之后将剩余的直接加到result
        while i < n:
            result.append(intervals[i])
            i += 1
        return result
