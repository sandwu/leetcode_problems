


class Solution(object):
    """
    这道题就是不知道基线条件在哪？看了讨论区答案才恍然大悟，如果在set集合里有重复值，说明陷入了循环，
    此时还没有找到=1的值则说明永远找不到了，所以return False就行
    Runtime: 28 ms, faster than 50.47% of Python online submissions for Happy Number.
    Memory Usage: 11.7 MB, less than 5.12% of Python online submissions for Happy Number.
    """
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mem = set()
        while n != 1:
            n = sum([int(n) ** 2 for n in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True