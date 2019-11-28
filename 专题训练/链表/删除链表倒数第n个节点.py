
#19


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    定义快慢指针，让快指针先跑n个格，这样当快指针跑完的时候，慢指针刚好停在从end开始的n个格，然后直接跳过即可
    Runtime: 16 ms, faster than 95.44% of Python online submissions for Remove Nth Node From End of List.
    Memory Usage: 11.8 MB, less than 26.64% of Python online submissions for Remove Nth Node From End of List.
    """
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head
        #遍历n，是的fast位于正数第n个节点
        for _ in range(n):
            fast = fast.next
        #当fast为None，索命要删除的节点是第一个节点，所以此时直接返回head.next，即跳过了第一个节点
        if not fast:
            return head.next
        #然后同时跑快慢指针，当快指针的next为None时，即说明到达了最后一个节点，此时将slow的写一个节点跳过即可
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


class Solution2(object):
    """
    用递归来完成，这个思路也是很强。当递归到链表结尾时，此时的i即表示最后1个数的开始索引即1，当i>n，即表示位于要删除的前一位，
    然后跳过即表示删除。最后再判断当n过大的情况，直接反馈head.next
    Runtime: 24 ms, faster than 62.50% of Python online submissions for Remove Nth Node From End of List.
    Memory Usage: 11.9 MB, less than 7.94% of Python online submissions for Remove Nth Node From End of List.
    """
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next