

class Solution(object):
    """
    看到找括号，第一反应就是通过stack来做，先进后出的数据结构完美解决，每次到右括号时判断左括号和右括号是否一致就行了，
    因为([ )]明显不存在，一定要是([])才行，所以每次pop()最先的就行了。
    Runtime: 24 ms, faster than 54.47% of Python online submissions for Valid Parentheses.
    Memory Usage: 12 MB, less than 5.20% of Python online submissions for Valid Parentheses.

    """
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right, stack= "({[", ")}]", []
        for item in s:
            if item in left:
                stack.append(item)
            else:
                if not stack or left.find(stack.pop()) != right.find(item):
                    return False
        return not stack

class Solution2(object):
    """
    讨论区的另一种解法，用字典来做，本质是一致的~
    Runtime: 24 ms, faster than 54.47% of Python online submissions for Valid Parentheses.
Memory Usage: 12.1 MB, less than 5.20% of Python online submissions for Valid Parentheses.
    """
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []