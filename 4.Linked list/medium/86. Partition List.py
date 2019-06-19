# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    这个解法太简洁易懂了！一开始我的想法就是只定义一条链表，但我发现没办法插入小于x的值到链表最前方，
    看到这个解法直接定义两条链表，小的归小的，大的归大的，最后合并即可，简直太强！
    Runtime: 20 ms, faster than 90.18% of Python online submissions for Partition List.
    Memory Usage: 11.8 MB, less than 68.50% of Python online submissions for Partition List.
    """
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        l1 = h1 = ListNode(0)
        l2 = h2 = ListNode(0)
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = h2.next
        return h1.next