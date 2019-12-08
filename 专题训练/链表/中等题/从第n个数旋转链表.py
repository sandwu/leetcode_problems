

# 61

class Solution:
    def rotateRight(self, head, k):
        n,pre,current = 0, None, head #pre服务于最后的循环，current来让pre指向最后的节点
        while current:
            pre,current = current,current.next
            n += 1 #可以记为一种求链表长度的方法

        while not n or not k%n: #k%n表明如果k和总长度一致，则无须反转
            return head

        dummy = head
        for _ in range(n - k%n -1): #取要反转的前一个数
            dummy = dummy.next

        curr = dummy.next #这个数就是反转后的head
        pre.next = head #原先指向null，将其指向当前的head
        dummy.next = None #原有的dummy.next指向反转后的head，所以将当前的指向尾节点

        return curr

