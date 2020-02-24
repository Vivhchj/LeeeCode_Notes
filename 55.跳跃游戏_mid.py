# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个位置。

# 示例 1:
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

# 示例 2:
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

### Solution1:贪心算法1
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 如果当前位置在max_p范围内且跳跃数大于0，据此更新最大索引，后移1位继续判断，直到最大索引大于等于len(nums)
        max_idx = len(nums)-1
        max_p = nums[0]
        # 遍历数列，每次判断是否更新max_p
        for i in range(1, max_idx):
            # 如果索引在max_p范围内，更新max_p
            if max_p >= i:
                max_p = max(max_p, i+nums[i])
                # 更新的max_p如果已经大过max_idx，判定为True
                if max_p >= max_idx:
                    break
        return True if max_p>=max_idx else False

### Solution2：贪心算法2，由后往前遍历
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # p表示已知能达到末尾的最小索引
        p = len(nums)-1
        # 由后往前遍历
        for i in range(p, -1, -1):
            if nums[i]+i>=p:
                p = i
        # 如果最小索引是0，即为True；否则False
        return p==0

