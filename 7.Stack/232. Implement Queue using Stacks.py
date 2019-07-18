

class MyQueue(object):
    """
    同225解法，用deque定义一个queue
    Runtime: 16 ms, faster than 76.75% of Python online submissions for Implement Queue using Stacks.
    Memory Usage: 11.9 MB, less than 6.76% of Python online submissions for Implement Queue using Stacks.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.s = deque()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.s.appendleft(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.s.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.s:return self.s[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not len(self.s)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()