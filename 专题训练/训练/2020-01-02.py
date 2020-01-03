

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

    def deletenth(self,head,k):
        slow = fast = head
        for _ in range(k):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

    def palindLink(self,head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #如果是3个则位于第2个，如果是4个则位于第3个
        prev = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr
        while curr:
            if curr.val != head.val:
                return False
            curr = curr.next
            head = head.next
        return True


