

#237
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    链表的删除就是指针的跳过，所以直接当前的node等于下个指针的值，然后跳过下个指针
    Runtime: 28 ms, faster than 66.40% of Python online submissions for Delete Node in a Linked List.
    Memory Usage: 12.4 MB, less than 24.28% of Python online submissions for Delete Node in a Linked List.
    """
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next