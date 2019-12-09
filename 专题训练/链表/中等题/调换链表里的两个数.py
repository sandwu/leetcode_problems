

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        curr = dummy = ListNode(0)
        dummy.next = head
        while dummy.next and dummy.next.next:
            a = dummy.next  #定义两个变量来接收，方便后续的循环调用
            b = dummy.next.next
            dummy.next, b.next, a.next = b, a, b.next #将dummy->a->b->b.next 转为dummy->b->a->b.next
            dummy = a #将指针转到调换后的第二个数，以便下一轮调换开始
        return curr.next