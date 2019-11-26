


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverslist(self,head):
        prev = None
        while head:
            curr = head
            head.next = prev
            head = head.next
            prev = curr
        return prev