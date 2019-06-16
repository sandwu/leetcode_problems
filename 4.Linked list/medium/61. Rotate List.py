
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    题目需要根据给定的数字依次反转链表，根据如下代码还是蛮清晰的，先求出总长度n，然后求出需要从
    哪个位置开始反转，要注意的是k%n来求余避免k>n的情况！接着通过tail=tail.next找到开始反转的上一个位置。
    比较难理解的是最后一步：先指定开始反转的tail.next，然后把该链表的tail.next重置为None，这样返回的结果就截止在反转，
    最后再把pre这原本指向链表最后位置的重置到开头，形成一个循环！
    Runtime: 20 ms, faster than 95.00% of Python online submissions for Rotate List.
    Memory Usage: 11.6 MB, less than 94.65% of Python online submissions for Rotate List.
    """
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        n ,pre ,current = 0 ,None ,head
        while current:
            pre ,current = current ,current.next
            n += 1

        while not n or not k % n:
            return head

        tail = head
        for i in range( n - k % n -1):
            tail = tail.next

        next, tail.next, pre.next = tail.next, None, head
        return next