



class MinStack(object):
    """
    题意是要求定义一个栈，还要满足以常数时间随时获取栈的最小值
    需要注意的是当入栈和出栈时，最小值也要随着变化！所以可以在入栈的时候做个手脚：即每次入栈入的
    是元祖，该元祖就维护着最小值和当前入栈的值。然后再拿top和Min时要注意分别拿的是元祖的入栈值和最小值
    Runtime: 64 ms, faster than 38.24% of Python online submissions for Min Stack.
    Memory Usage: 15.8 MB, less than 43.61% of Python online submissions for Min Stack.
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        curmin = self.getMin()
        if self.getMin() == None or x < self.getMin():
            curmin = x
        self.s.append((x,curmin))

    def pop(self):
        """
        :rtype: None
        """
        self.s.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.s) == 0:
            return None
        else:
            return self.s[len(self.s) - 1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.s) == 0:
            return None
        else:
            return self.s[len(self.s) - 1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()