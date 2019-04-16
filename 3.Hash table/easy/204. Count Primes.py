


class Solution(object):
    """
    通过厄尔多塞法来判断，按照正常的素数判断是当数为n时，在(2,n)之间都不能整除，则为素数，那时间
    复杂度过高。厄尔多塞法则通过计算在根号n的范围内，其每个值的乘积一定不是素数，当超过根号n后，直接取
    剩余的值即可，效率也是非常的可观
    Runtime: 272 ms, faster than 83.27% of Python online submissions for Count Primes.
    Memory Usage: 34.9 MB, less than 59.02% of Python online submissions for Count Primes.
    """
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in range(2,int(n ** 0.5) + 1):
            if res[i]:
                res[i*i:n:i] = [0] * len(res[i*i:n:i])
        return sum(res)