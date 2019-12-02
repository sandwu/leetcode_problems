

#定义一个链表
class Node:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution:
    #反转链表
    def reverseList(self,head):
        """
        用倒插法，即将头部变成尾部，然后逐步转换；注意边界！
        :param head:
        :return:
        """
        prev = None #先定义反转后的尾节点
        while head:
            curr = head #curr变量用于指向反转链表
            head = head.next #head变量用于指向正向链表
            curr.next = prev #将curr的next指定为prev，一开始是尾节点
            prev = curr #将尾节点往前推移
        return prev

    #寻找中间节点
    def middleNode(self,head):
        """
        定义快慢指针，快的跑两步，慢的跑一步，当快的跑到终点，慢到达的点即是答案
        :param head:
        :return:
        """
        slow = fast = head
        while fast and fast.next: #注意边界是fast和fast.next都存在
            slow = slow.next
            fast = fast.next.next
        return slow

    #检测离岸边中换的存在
    def cycleList(self,head):
        """
        同寻找中间节点的原理，定义快慢指针，在快的跑到终点过程里，检测慢指针和快指针是否相同即可
        :param head:
        :return:
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if slow == fast:
                return True
        return False

    #删除链表倒数第n个点
    def findNthFromEnd(self,head,n):
        """
        定义快慢指针，先让快指针跑n个点，然后当快指针到达终点，此时慢指针所在的位置即是倒数第n个节点
        此时就是链表经典的删除操作：node.next = node.next.next
        :param head:
        :param n:
        :return:
        """
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        while fast.next:#注意边界是fast.next
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next #要删除slow.next，即将其指向slow,next.next
        return head

    #合并两个有序链表
    def mergeTwoLists(self,l1,l2):
        """
        合并两个有序链表的方法和归并排序原理上是一致，不过要用到链表的方式来处理
        链表的方式通过定义第三条链表作为head，然后逐步把li和l2里小的加入到head里，最后把剩余的一条合并即可
        :param l1:
        :param l2:
        :return:
        """
        dummy = curr = Node(0) #定义两个head节点，dummy用于指向头结点，curr用于指向l1和l2合并上来的当前节点
        while l1 and l2:#这里的l1和l2是指代头结点
            if l1.val <= l2.val:
                curr.next = l1 #将curr.next指向小的那个节点
                l1 = l1.next #然后将对应的有序链表下移一位
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next #将合并后的链表下移一位
        curr.next = l1 or l2 #最后合并还存活的链表即可
        return dummy.next

    #判断链表是否回文字符串
    def isPalindrome(self, head):
        """
        本质是通过快慢节点将链表拆分成两部分(原来等同于查找链表的中间节点)
        然后将后半部分反转(等同于反转链表)
        最后将前半部分和后半部分一一比较即可
        :param head:
        :return:
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next #到这里完成链表的拆分

        prev = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr  #到这里完成链表的反转

        while prev: #接下来就是一一比较
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True

    #删除单链表的指定节点
    def deleteNode(self, node):
        """
        因为是单链表，所以无法找到它的前驱节点，这里提供了绕过当前节点的方法
        即将该node的后一个节点的值赋予该节点，然后删除后一个节点！
        :param node:
        :return:
        """
        node.val = node.next.val
        node.next = node.next.next