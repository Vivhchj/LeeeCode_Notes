### content:
### 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
### 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

### 示例:
### 给定 1->2->3->4, 应返回 2->1->4->3.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

### solution1:递归函数，O(n)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        h = ListNode(-1)
        h.next = head
        def exchpairs(a: ListNode, b: ListNode):
            # 如果当前节点以及下一节点均不为空
            if b and b.next:
                c = b.next
                d = c.next
                a.next = c
                b.next = d 
                c.next = b
                exchpairs(b, b.next)
        
        exchpairs(h, head)
        return h.next

### solution2:while loop
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        prehead = ListNode(-1)
        prehead.next = head
        c = prehead
        # 直接用前置节点c进入循环进行操作
        while c.next and c.next.next:
            a,b = c.next,c.next.next
            c.next, a.next = b, b.next
            b.next = a
            # 置换完成后c再后移两位
            c = c.next.next
                      
        return prehead.next
