

# 61

class Solution:
    def rotateRight(self, head, k):
        n,pre,current = 0, None, head #pre服务于最后的循环，current来让pre指向最后的节点
        while current:
            pre,current = current,current.next
            n += 1 #可以记为一种求链表长度的方法

        while not n or not k%n: #k%n表明如果k和总长度一致，则说明不用旋转，此时直接返回head即可
            return head