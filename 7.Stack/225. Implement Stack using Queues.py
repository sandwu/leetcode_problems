


class MyStack(object):
    """
    题意是要求定义一个stack：然后提供push、pop、top、empty等方法
    因为collections的deque支持appendleft和popleft，所以特别适合做队列或者栈！
    Runtime: 20 ms, faster than 52.86% of Python online submissions for Implement Stack using Queues.
    Memory Usage: 11.9 MB, less than 24.57% of Python online submissions for Implement Stack using Queues.
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.s = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.s.appendleft(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.s:
            return self.s.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.s:
            return self.s[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not len(self.s)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()