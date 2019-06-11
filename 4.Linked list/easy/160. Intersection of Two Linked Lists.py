# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    该解法就是简单粗暴，因为需要找到两链表的相同点，就不断地循环遍历两者，当二者相等即可返回。当其中一个为None时会继续
    循环，直到两个都为None了那就返回任意一个。要注意的是当一个链表走到结尾时，需要去走另一个链表，这是因为两个链表的长度不等，
    只有走到另一个链表才能使第二次遍历二者长度相等，从而能找到相等的点
    Runtime: 196 ms, faster than 90.38% of Python online submissions for Intersection of Two Linked Lists.
    Memory Usage: 41.8 MB, less than 56.97% of Python online submissions for Intersection of Two Linked Lists.
    """
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        pa = headA
        pb = headB

        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa



class Solution2(object):
    """
    They must have same nodes after the intersection point.
    L1+L2 must have same tail from the intersection point as L2 + L1. For example,
    L1 = 1,2,3
    L2 = 6,5,2,3

    L1+L2 = 1,2,3,6,5,2,3
    L2+L1 = 6,5,2,3,1,2,3

    To implement L1+L2 as well as L2+L1, we can simply jump to another list's head
    after traveling through certain list.
    But, you need to notice that if the two lists have no intersection at all,
    you should stop after you've already checked L1+L2, so we need a flag jumpToNext to ensure we only traverse L1 + L2 once.

    Runtime: 188 ms, faster than 96.00% of Python online submissions for Intersection of Two Linked Lists.
    Memory Usage: 41.8 MB, less than 41.84% of Python online submissions for Intersection of Two Linked Lists.
    """
    def getIntersectionNode(self, headA, headB):
        ptA, ptB, jumpToNext = headA, headB, False
        while ptA and ptB:
            if ptA == ptB:
                return ptA
            ptA, ptB = ptA.next, ptB.next
            if not ptA and not jumpToNext:
                ptA, jumpToNext = headB, True
            if not ptB:
                ptB = headA
        return None