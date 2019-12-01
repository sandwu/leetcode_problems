#234


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    钻了个漏洞，把链表硬改成列表来完成！
    Runtime: 92 ms, faster than 21.88% of Python online submissions for Palindrome Linked List.
    Memory Usage: 31.1 MB, less than 16.84% of Python online submissions for Palindrome Linked List.
    """
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]

class Solution2(object):
    """
    相关的注释下面写的很清楚，先取到中位数slow，然后根据slow将后半段反转，接着一一比较即可
    Runtime: 68 ms, faster than 89.71% of Python online submissions for Palindrome Linked List.
    Memory Usage: 30.9 MB, less than 52.98% of Python online submissions for Palindrome Linked List.
    """
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        while node: # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True