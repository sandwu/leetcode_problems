
class ListNode:
    def __init__(self,x):
        self.val = x
        self.Next = None

class Solution:
    def fromNthRveviseList(self,head,k):
        curr = dummy = head
        n = 0
        while dummy:
            pre = dummy  # 当结束时pre指向最后一个节点
            dummy = dummy.next
            n += 1 #获取总长度

        while not n or not k%n:
            return head #如果整除，说明无须翻转

        for _ in range(n-k%n-1):
            curr = curr.next #因为是倒数k个，这里是到达倒数k的上一个数

        current = curr.next
        pre.next = head
        curr.next = None

        return current

    def removeDuplicateNode(self, head):
        curr = dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head.next = head.next.next
                head = head.next
                dummy.next = head
            else:
                head = head.next
                dummy = dummy.next
        return curr.next

    def twoListSum(self, l1, l2):
        curr = ListNode(0)
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
        return curr.next

    def swapTwoNumList(self,head):
        curr = dummy = ListNode(0)
        dummy.next = head
        while dummy.next and dummy.next.next:
            a = dummy.next
            b = dummy.next.next
            dummy.next, b.next, a.next = b,a,a.next
            dummy = a
        return dummy.next
