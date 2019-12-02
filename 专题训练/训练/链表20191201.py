
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Linklist:
    def reverseLink(self,head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def cycleList(self,head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def middleNode(self,head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        return slow

    def findNthFromEnd(self,head, n):
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head

    def isPalindrom(self,head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr

        while prev or head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True

    def mergeSortList(self, l1, l2):
        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
        dummy.next = l1 or l2
        return curr


    def deletenode(self,node):
        node.val = node.next.val
        node.next = node.next.next

    def deleteval(self,head,val):
        new_head = ListNode(0)
        new_head.next = head
        slow, fast = new_head, head
        while fast:
            if fast.val != val:
                slow.next.val = fast.val
                slow = slow.next
            fast = fast.next
        slow.next = None
        return new_head.next
