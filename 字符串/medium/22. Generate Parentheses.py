

class Solution(object):
    """
    这个递归用的真的有水平，在每次调用自身的时候，如果left<right，则相当于两条分支下的递归，直到基线条件返回
    Runtime: 40 ms, faster than 17.47% of Python online submissions for Generate Parentheses.
    Memory Usage: 12.3 MB, less than 5.02% of Python online submissions for Generate Parentheses.
    """
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p,
            return parens
        return generate('', n, n)



class Solution2(object):
    """
    另一种形式
    Runtime: 28 ms, faster than 46.17% of Python online submissions for Generate Parentheses.
    Memory Usage: 12.2 MB, less than 5.02% of Python online submissions for Generate Parentheses.
    """
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left-1, right): yield q
                for q in generate(p + ')', left, right-1): yield q
        return list(generate('', n, n))