

#21



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    递归的思路还是比较清晰的，基线是l1和l2都存在，当一方不存就返回另一方的全部；未到基线时，就逐一比对，大的归到l1，
    小的归到l2，因为每次交换都是节点交换，所以l1.next可以同时包含l1和l2的值
    Runtime: 24 ms, faster than 98.30% of Python online submissions for Merge Two Sorted Lists.
    Memory Usage: 11.8 MB, less than 60.71% of Python online submissions for Merge Two Sorted Lists.
    """
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and l2:
            if l1.val > l2.val:
                l1 ,l2 =l2 ,l1
            l1.next  = self.mergeTwoLists(l1.next ,l2)
        return l1 or l2


class Solution2(object):
    """
    非递归的解决思路如下，相当于在while里拆解了递归思路
    Runtime: 24 ms, faster than 98.30% of Python online submissions for Merge Two Sorted Lists.
    Memory Usage: 11.7 MB, less than 69.12% of Python online submissions for Merge Two Sorted Lists.
    """
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

