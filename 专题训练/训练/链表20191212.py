
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
        pass

    def twoListSum(self, l1, l2):
        pass

    def swapTwoNumList(self,head):
        pass