### content:
### 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
### 示例：
### 给定一个链表：1->2->3->4->5, 和 n = 2.
### 返回链表：1->2->3->5.
### 说明:给定的 n 保证是有效的。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

### solution1:
### 我的思路：首先将链表从头遍历到尾，然后从尾回溯，回溯时判断每个节点是否是倒数第n个节点
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ## 回溯函数
        def rtnnode(l1:ListNode, l2:ListNode):
            flag = 1 if not l2.next else rtnnode(l2, l2.next)+1
            ## 如果是倒数第n个节点进行删除
            if flag==n:
                l1.next = l2.next if n>1 else None
            return flag
        if head.next:
            ## 判断需要删除的是否是head节点 
            if n==rtnnode(head, head.next)+1:
                head = head.next
        ## 链表长度为1时若n为1则除掉head节点
        elif n==1:
            head = None
        return head

### solution2:两次遍历
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ln_len = 0
        l = head
        ## 得到链表全长ln_len
        while l:
            ln_len += 1
            l = l.next
        ## 如果需要删除的是第一个节点，则删除第一个节点，令head = head.next或None(考虑链表只有一个节点的情况)
        if ln_len==n:
            head = head.next if head.next else None
        ## 否则，遍历到需要删除的节点的前一个结点l，令l.next指向其后的第二个节点或None(考虑需要删除的节点是末尾节点的情况)
        else:
            l = head
            for i in range(ln_len-n-1):
                l = l.next
            m = l.next
            l.next = m.next if m.next else None
        return head

### solution3:一次遍历
### 思路：遍历一次，但是安排两个节点，节点间隔为n，当先出发的节点到达末尾时，删除后出发节点后面的那个节点
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l1,l2 = head,head
        i = 0
        ## 使l1与l2间隔n个节点前进
        while l1.next:
            l1 = l1.next
            if i>=n:
                l2 = l2.next
            i += 1
        ## i+1表示链表实际长度，实际长度==n时，l2并未移动，需删除头节点
        if i+1==n:
            head = head.next
        else:
            temp = l2.next
            l2.next = temp.next
        return head
