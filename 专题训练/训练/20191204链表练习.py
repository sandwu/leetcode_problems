class ListNode:
    def __init__(self,x):
        self.x = x
        self.next = None


class LinkedList:
    def removedupplicate(self,head):
        #有序链表，删除重复字段，每个数字仅留一次
        dummy  = ListNode(0)
        dummy.next = head
        while head:
            while head.next and head.val == head.next.val:
                head.next = head.next.next
            head = head.next
        return dummy.next


    def removedupplication2(self,head):
        #有序链表，目的是删除所有的重复数，包括连唯一的那个也删除
        dummy = curr = ListNode(0)
        curr.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                dummy.next = head
            else:
                head = head.next
                dummy = dummy.next
        return curr.next