

#链表回顾



class ListNode:
    def __init__(self,x):
        self.val = x
        self.Next = None


class Solution:
    def reverseLink(self,head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return curr

    def middleLink(self,head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def cycleLink(self,head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def deleteNode(self,node):
        node.val = node.next.val
        node.next = node.next.next

    def deleteval(self,head,val):
        prev = dummy = ListNode(None)
        dummy.next = head
        while head:
            if head.val == val:
                dummy.next = head.next
            else:
                dummy = dummy.next
            head = head.next
        return prev.next

    def sortLinkList(self,l1,l2):
        curr = dummy = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2.val
                l2 = l2.next
            dummy = dummy.next
        dummy.next = l1 or l2
        return curr.next
