

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    pre is the previous node. Since the head doesn't have a previous node, I just use self instead. Again,
    a is the current node and b is the next node.To go from pre -> a -> b -> b.next to pre -> b -> a -> b.next
    Runtime: 16 ms, faster than 93.29% of Python online submissions for Swap Nodes in Pairs.
    Memory Usage: 11.8 MB, less than 50.85% of Python online submissions for Swap Nodes in Pairs.
    """
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre,pre.next = self,head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b,a,b.next
            pre = a
        return self.next