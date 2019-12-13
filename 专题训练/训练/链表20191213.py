



class ListNode:
    def __init__(self,x):
        self.val = x
        self.Next = None

class Solution:
    def fromNthRveviseList(self,head,k):
        dummy = head
        n = 0
        while dummy:
            pre,dummy = dummy,dummy.next
            n += 1

        while not n or k%n:
            return head

        current = head
        for _ in range(n - k%n -1 ):
            current = current.next

        res = current.next
        pre.next = head
        current.next = None
        return res

    def removeDuplicateNode(self,head):
        dummy = curr = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head.next = head.next.next
                head = head.next
            else:
                dummy.next = head
                head = head.next
                dummy = dummy.next
        return curr.next



    def swapTwoNum(self,head):
        dummy = curr = ListNode(0)
        dummy.next = head
        while dummy.next and dummy.next.next:
            a = dummy.next
            b = dummy.next.next
            dummy.next,b.next,a.next = b,a,b.next
            dummy = a
        return curr.next

    def twoListSum(self,l1,l2):
        curr = dummy = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 += l1.val
                l1 = l1.next
            if l2:
                v2 += l2.val
                l2 = l2.val
            carry, val = divmod(v1+v2+carry,10)
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next


    def reverseList(self,head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev


