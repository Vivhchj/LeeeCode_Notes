# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 num1 成为一个有序数组。

# 说明:
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

# 示例:
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 输出: [1,2,2,3,5,6]


###Solution: 双指针，从后往前排序; 由后往前是因为nums1末尾是与nums2等长的0元素，不需额外内存用于调换位置
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 索引idx和末尾开始遍历比较的指针1 2
        idx, idx1, idx2 = m+n-1, m-1, n-1
        while idx >= 0:
            # 当nums1未遍历完
            if idx1 >= 0:
                # 如果nums2也未遍历完，正常操作
                if idx2 >= 0:
                    if nums1[idx1] >= nums2[idx2]:
                        nums1[idx] = nums1[idx1]
                        idx1 -= 1
                    else:
                        nums1[idx] = nums2[idx2]
                        idx2 -= 1
                # nums2遍历完，直接结束，因为nums1前面的升序部分不需再变化
                else:
                    break
            # nums1遍历完而nums2尚有剩余，直接将nums2的剩余部分放到nums1
            elif idx2 >= 0:
                nums1[idx] = nums2[idx2]
                idx2 -= 1
            # 两数组遍历结束后居然还有剩余，基本不会出现的情况
            else:
                print("length error")
            idx -= 1
