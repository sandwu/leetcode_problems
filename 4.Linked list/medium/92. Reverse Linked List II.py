# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    题目要求按照索引m和n将这之间的链表反转，所以思路很清晰，先定位到m的位置，然后对到n之间的链表用单链表反转
    也就是leetcode第206的方法来做，反转后指定链表的指向即可
    Runtime: 16 ms, faster than 92.06% of Python online submissions for Reverse Linked List II.
    Memory Usage: 12.1 MB, less than 11.07% of Python online submissions for Reverse Linked List II.
    """
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next

        # reverse the [m, n] nodes
        reverse = None
        cur = pre.next
        for i in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        pre.next.next = cur
        pre.next = reverse

        return dummyNode.next

