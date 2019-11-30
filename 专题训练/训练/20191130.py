


class Node:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution:
    def reverselist(self,head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def middlenode(self,head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def cyclenode(self,head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if slow == fast:
                return True
        return False

    def findnethfromend(self,head,n):
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head

    def mergetwolists(self,l1,l2):
        dummy = curr = Node(0)
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

    def isPalindrome(self, head):
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

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
