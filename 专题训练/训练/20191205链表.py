class ListNode:
    def __init__(self,x):
        self.x = x
        self.next = None


class LinkedList:
    def removeduplicates1(self,head):
        if not head:return
        node = head
        while node and node.next:
            while node.val == node.next.val:
                node.next = node.next.next
            node = node.next
        return head


    def removeduplicates2(self,head):
        dummy = curr = ListNode(0)
        dummy.next = head  # 如果只有一个元素的话
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                dummy.next = head
            else:
                dummy.next = head
                head = head.next
                dummy = dummy.next  # dummy的后移仅当不同的时候才能后移，因为最后一个元素无法判断
        return curr.next

    # def deractor(func):
#     def wrap(*args,**kwargs):
#         print("1111")
#         func(*args,**kwargs)
#         print("222")
#     return wrap
#
# @deractor
# def fun1(x,y):
#     print("x+y=",x+y)
#
# def login_require(role='DEV'):
#     def wrap(func):
#         def func1(*args,**kwargs):
#             if role == "DEV":
#                 print("1111")
#             elif role == 'RD':
#                 print("2222")
#             else:
#                 print("3333")
#             func(*args,**kwargs)
#         return func1
#     return wrap
#
# @login_require(role='asdasd')
# def fun2(x,y):
#     print("3*4=", x*y)
#
# fun1(3,4)
# fun2(3,4)


