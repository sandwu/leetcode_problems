
class Node:
    def __init__(self,x):
        self.val = x
        self.next = None


class LinkedList:
    def reverselist(self,head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def removeNthFromEnd(self,head,n):
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head

    def middlenode(self,head):
        pass

    def cyclelist(self,head):
        pass