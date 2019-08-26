

# Definition for singly-linked list.
from future.moves import collections


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    参考讨论区：https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/discuss/366319/JavaC%2B%2BPython-Greedily-Skip-with-HashMap
    题意是求链表里如果部分node相加为0，则移除这些node
    解法：定义链表dummy，从头到尾，将前面node到当前node的和依次作为key存储到seen(有序字典)
    然后遍历字典seen，做两件事：
        1.If it's a prefix that we've never seen, we set m[prefix] = cur.
        2.If we have seen this prefix, m[prefix] is the node we achieve this prefix sum.
        We want to skip all nodes between m[prefix] and cur.next (exclusive).
        So we simplely do m[prefix].next = cur.next.
    """
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        seen = collections.OrderedDict()
        while cur:
            prefix += cur.val
            node = seen.get(prefix, cur)
            while prefix in seen:
                seen.popitem()
            seen[prefix] = node
            node.next = cur = cur.next
        return dummy.next