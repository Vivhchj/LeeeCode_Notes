# 实现 int sqrt(int x) 函数。
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

# 示例 1:
# 输入: 4
# 输出: 2

# 示例 2:
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...，由于返回类型是整数，小数部分将被舍去。

### Solution:采用二分法思想，先指数扩张，再二分查找
### 平方根整数解，要满足 result^2 <= x < (result+1)^2
class Solution:
    def mySqrt(self, x: int) -> int:
        
        right = 1
        # 找到max_num^2>=x的max_num
        while right*right < x:
            right <<= 1
        left = right >> 1
        # 定位到result在[left,right]之间，在此范围内二分查找得到result
        while left < right:
            # 取到右中位数
            mid = (left + right + 1) >> 1
            # 当mid^2<=x时，result一定在[mid, right]之间
            if mid * mid <= x:
                left = mid
            # 当mid^2>x时，result一定在[left,mid-1]之间
            else:
                right = mid-1
        return left
         
        
