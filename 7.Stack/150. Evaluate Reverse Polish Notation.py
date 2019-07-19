import operator


class Solution(object):
    """
    题意是将后缀表达式转中缀表达式，利用python的eval来完成
    解法是依次往栈里加值，当碰到操作符，就pop出前两个数字计算，要注意的是如果是除法，python2和python3虽然整除方式分别是
    /和//，但是他们都是向下取整，这个当碰到是负数的情况，比如-1//2=-1，而题意是要求像C++一样是向0取整，所以这里除法是用了
    operator.truediv来完成
    Runtime: 100 ms, faster than 6.69% of Python online submissions for Evaluate Reverse Polish Notation.
    Memory Usage: 13.3 MB, less than 89.90% of Python online submissions for Evaluate Reverse Polish Notation.
    """
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '/':
                    res = int(operator.truediv(int(a), int(b)))
                else:
                    res = eval(a + token + b)
                stack.append(str(res))
        return int(stack.pop())



class Solution2(object):
    """
    上述eval速度很快，但是效率就不高，这里避免了eval的解法，效率提高了很多
    Runtime: 48 ms, faster than 98.25% of Python online submissions for Evaluate Reverse Polish Notation.
    Memory Usage: 13.7 MB, less than 11.78% of Python online submissions for Evaluate Reverse Polish Notation.
    """
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                    # here take care of the case like "1/-22",
                    # in Python 2.x, it returns -1, while in
                    # Leetcode it should return 0
                    if l*r < 0 and l % r != 0:
                        stack.append(l/r+1)
                    else:
                        stack.append(l/r)
        return stack.pop()