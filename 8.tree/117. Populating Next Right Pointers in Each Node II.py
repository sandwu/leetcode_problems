


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections


class Solution:
    """
    就是把每层的节点放到一个队列里，把队列的每个元素进行弹出的时候，
    如果它不是该层的最后一个元素，那么把它指向队列中的后面的元素（不把后面的这个弹出）
    """
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        queue = collections.deque()
        queue.append(root)
        while queue:
            _len = len(queue)
            for i in range(_len):
                node = queue.popleft()
                if i < _len - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
