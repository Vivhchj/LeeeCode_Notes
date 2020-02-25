# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。

# 示例 1:
# 输入: [1,2,9]
# 输出: [1,3,0]
# 解释: 输入数组表示数字 130。

### Solution:此题要注意有9进位的情况
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        # 倒序遍历数字序列模拟进位情况，如果是九，则需要进位，当前位变为0；否则直接在当前位+1并结束循环；
        # 当序列全部是9时，会致使digits[0]=0，因此在循环结束后，我们判断如果digits[0]=0，则需要在前面加一个数字1
        for i in range(length-1, -1, -1):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i] += 1
                break
        return [1]+digits if digits[0]==0 else digits
