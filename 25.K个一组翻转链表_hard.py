### content:
### 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
### k 是一个正整数，它的值小于或等于链表的长度。
### 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

### 示例 :
### 给定这个链表：1->2->3->4->5
### 当 k = 2 时，应当返回: 2->1->4->3->5
### 当 k = 3 时，应当返回: 3->2->1->4->5

### 说明 :
### 你的算法只能使用常数的额外空间。
### 是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

### solution:
### 思路：
# 所谓的颠翻转其实可以理解为，规定指向下一轮k个节点的指针h，将后面顺序遍历到的k个节点依次放到h.next，这样就可以达到翻转的效果
# 即将 h->……->i->j->……->k 变成 h->i->……->j->……->k
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 返回第k个节点，作为下一次翻转的头节点h
        def pair_rev(h) -> ListNode:
            # 记下此段的第一个节点记为f，需要前置的节点是f.next(即节点g)
            f = h.next
            for _ in range(k-1):
                g = f.next
                f.next = g.next
                g.next = h.next
                h.next = g
            return f
        # 得到链表的长度，进而得到需要翻转的次数
        flag,n = head,0
        while flag:
            flag = flag.next
            n += 1
        times = n//k
        
        # 新建一个节点指向链表
        a = ListNode(-1)
        a.next = head
        h0 = a
        for _ in range(times):
            h0 = pair_rev(h0)
        return a.next
