

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    单链表反转，是很经典的题了，该题解法是倒插头，curr的next是prev，而prev指向curr(即反转指向上一个)，当
    prev = 5的时候，curr.next指向4，所以直接返回prev即可完成链表的反转
    Runtime: 24 ms, faster than 84.08% of Python online submissions for Reverse Linked List.
    Memory Usage: 13.6 MB, less than 65.73% of Python online submissions for Reverse Linked List.
    """
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev


class Solution2(object):
    """
    递归思路：过程一步步写出来和上面的相差不大，就是让node.next不断指向prev，而prev的值又是由node传出，
    即当prev递归到返回时(即5)，node.next刚好指向4，此时返回prev，即返回全部
    Runtime: 16 ms, faster than 99.10% of Python online submissions for Reverse Linked List.
    Memory Usage: 18.7 MB, less than 5.04% of Python online submissions for Reverse Linked List.
    """
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)