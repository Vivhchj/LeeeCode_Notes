### content:
### 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
### 示例：
### 输入：1->2->4, 1->3->4
### 输出：1->1->2->3->4->4


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

### solution1:从头找l1和l2较小的加入h链表中，有一个遍历到末尾则直接将另一个拼接到h.next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        h = ListNode(0)
        l = h
        while l1 and l2:
            if l1.val <= l2.val:
                l.next = l1
                l = l.next
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
                l = l.next
        l.next = l1 if l1 else l2
        return h.next


### solution2:带佬的递归方法
## 前向按照大小顺序往下遍历，返回时则按照顺序从末尾排列好
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        ## 保留l1和l2的较小值，下一个值则进入下一次判断
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
