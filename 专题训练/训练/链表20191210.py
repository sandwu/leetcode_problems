
class ListNode:
    def __init__(self,x):
        self.val = x
        self.Next = None

class Solution:
    def fromNthRveviseList(self,head,k):
        n, pre, current = 0, None, head  # pre服务于最后的循环，current来让pre指向最后的节点
        while current:
            pre, current = current, current.next
            n += 1  # 可以记为一种求链表长度的方法

        while not n or not k % n:  # k%n表明如果k和总长度一致，则无须反转
            return head

        dummy = head
        for _ in range(n - k % n - 1):  # 取要反转的前一个数
            dummy = dummy.next

        curr = dummy.next  # 这个数就是反转后的head
        pre.next = head  # 原先指向null，将其指向当前的head
        dummy.next = None  # 原有的dummy.next指向反转后的head，所以将当前的指向尾节点

        return curr


    def removeDuplicateNode(self,head):
        dummy = curr = ListNode(0)
        while head:

            pass

    def twoListSum(self,l1,l2):
        carry = 0
        curr = dummy = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry,val = divmod(v1+v2+carry,10)
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def swapTwoNumList(self,head):
        pass