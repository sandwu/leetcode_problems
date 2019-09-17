

"""
Example 1:
Input: s = "(abcd)"
Output: "dcba"

Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"

Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"

Example 4:
Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"
"""


class Solution(object):
    """
    通过左括号占位符，将数据每碰到右括号就进行倒置，巧妙处在于处理右括号时res[len(res)-2],
    """
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ['']
        for c in s:
            if c == '(':
                res.append('')
            elif c == ')':
                res[len(res) - 2] += res.pop()[::-1]
            else:
                res[-1] += c
        return "".join(res)

class Solution2(object):
    def reverseParentheses(self, s):
        opened = []
        pair = {}
        for i, c in enumerate(s):
            if c == '(':
                opened.append(i)
            if c == ')':
                j = opened.pop()
                pair[i], pair[j] = j, i
        res = []
        i, d = 0, 1
        while i < len(s):
            if s[i] in '()':
                i = pair[i]
                d = -d
            else:
                res.append(s[i])
            i += d
        return ''.join(res)


a = Solution()
s = "(u(love)i)"
print(a.reverseParentheses(s))