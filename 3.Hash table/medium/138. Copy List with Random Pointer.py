

# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    """
    先构造字典，将老链表和新链表一一对应，这样就构造了一个纯next的链表，然后再循环即可
    Runtime: 392 ms, faster than 33.67% of Python online submissions for Copy List with Random Pointer.
    Memory Usage: 14.6 MB, less than 100.00% of Python online submissions for Copy List with Random Pointer.
    """
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        nodeDict = dict()
        dummy = Node(0, None, None)
        nodeDict[head] = dummy
        newHead, pointer = dummy, head
        while pointer:
            node = Node(pointer.val, pointer.next, None)
            nodeDict[pointer] = node
            newHead.next = node
            newHead, pointer = newHead.next, pointer.next
        pointer = head
        while pointer:
            if pointer.random:
                nodeDict[pointer].random = nodeDict[pointer.random]
            pointer = pointer.next
        return dummy.next

