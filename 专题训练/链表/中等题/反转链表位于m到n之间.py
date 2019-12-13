

#92
"""
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

"""

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self,head,m,n):
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

        pre.next.next = cur  #prev.next原本指向m位置，m位置反转后的next指向n.next也就是cur
        pre.next = reverse  #prev.next从指向m位置变更成指向n位置

        return dummyNode.next


    def reverseList2(self,head,m,n):
        dummy = res = ListNode(0)
        dummy.next = head
        for _ in range(m-1):
            dummy = dummy.next

        prev = None
        reverse = dummy.next
        for _ in range(n-m+1):
            curr = reverse
            reverse = reverse.next
            curr.next = prev
            prev = curr  #到最后reverse位于n的后一位，prev位于n

        dummy.next.next = reverse
        dummy.next = prev

        return res.next