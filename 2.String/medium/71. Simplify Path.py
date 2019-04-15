

class Solution(object):
    """
    用栈来完成，如果是..返回上级目录就出栈，如果不是空或者.就进栈，整个时间复杂度O(n)
    Runtime: 24 ms, faster than 94.46% of Python online submissions for Simplify Path.
    Memory Usage: 11.8 MB, less than 6.02% of Python online submissions for Simplify Path.
    """
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dirs = path.split('/')
        stack = []
        for dir in dirs:
            if not dir or dir == '.':
                continue
            elif dir == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        return '/'+'/'.join(stack)