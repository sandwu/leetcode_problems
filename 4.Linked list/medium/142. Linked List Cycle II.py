# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    题意是要求判断是否有环，详细的验证还是比较复杂的，参考这篇：https://blog.csdn.net/l294265421/article/details/50478818
    Runtime: 40 ms, faster than 85.81% of Python online submissions for Linked List Cycle II.
    Memory Usage: 18.1 MB, less than 76.74% of Python online submissions for Linked List Cycle II.
    """
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        else:
            return None
        while head != slow:  #当相遇的时候，慢指针巨鹿环节点的距离和head距离环节点的距离一致！
            slow = slow.next
            head = head.next
        return head


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2(object):
    """
    直接用python的set来保存link节点node，当碰到循环节点时，即得到结果
    Runtime: 32 ms, faster than 98.60% of Python online submissions for Linked List Cycle II.
    Memory Usage: 18.8 MB, less than 10.02% of Python online submissions for Linked List Cycle II.
    """
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        visited = set()
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return None


