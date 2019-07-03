

class Solution(object):
    """
    参考博文：https://blog.csdn.net/fuxuemingzhu/article/details/80658810
    Runtime: 12 ms, faster than 97.06% of Python online submissions for Permutation Sequence.
    Memory Usage: 11.7 MB, less than 57.80% of Python online submissions for Permutation Sequence.

    """
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = range(1, n + 1)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation


class Solution2(object):
    """
    Runtime: 12 ms, faster than 97.06% of Python online submissions for Permutation Sequence.
    Memory Usage: 11.7 MB, less than 84.10% of Python online submissions for Permutation Sequence.
    """
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = ''
        fact = [1] * n
        num = [str(i) for i in range(1, 10)]
        for i in range(1, n):
            fact[i] = fact[i - 1] * i
        k -= 1
        for i in range(n, 0, -1):
            first = k // fact[i - 1]
            k %= fact[i - 1]
            ans += num[first]
            num.pop(first)
        return ans
