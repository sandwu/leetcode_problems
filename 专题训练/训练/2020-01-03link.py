
#链表回顾2

class ListNode:
    def __init__(self,x):
        self.val = x
        self.Next = None


class Solution:
    def reversefromnth(self,head,k):
        n,prev,current = 0,None,head
        while current:
            prev,currnet = current,current.next
            n += 1

        while not n or not k%n:
            return head
        curr = head
        for _ in range(n-k%n-1):
            curr = curr.next

        dummy = curr.next
        curr.next = None
        prev.next = head
        return dummy

    def removeDuplicateNodes(self,head):
        curr = dummy = ListNode(None)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val==head.next.val:
                    head = head.next
                dummy.next = head
                head = head.next
            else:
                dummy = dummy.next
                head = head.next
        return curr.next

    def reversefrommton(self,head,m,n):
        dummy = res = ListNode(0)
        dummy.next = head
        for _ in range(m - 1):
            dummy = dummy.next

        prev = None
        reverse = dummy.next
        for _ in range(n - m + 1):
            curr = reverse
            reverse = reverse.next
            curr.next = prev
            prev = curr  # 到最后reverse位于n的后一位，prev位于n

        dummy.next.next = reverse
        dummy.next = prev

        return res.next

    def partitionLink(self,head,x):
        l1 = h1 = ListNode(0)
        l2 = h2 = ListNode(0)
        while head:
            if head.val <= x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l1.next = h2.next
        l2.next = None
        return h1.next

    def sortLink(self,head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = self.sortLink(slow.next)
        slow.next = None
        left = self.sortLink(head)
        return self.merge(left,right)

    def merge(self,left,right):
        dummy = curr =ListNode(None)
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left or right
        return dummy.next

    def sumoftwolink(self,l1,l2):
        dummy = curr = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def cycleList2(self,head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        while head != slow:
            slow,head = slow.next,head.next
        return head
