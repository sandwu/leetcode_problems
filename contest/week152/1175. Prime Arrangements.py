

#题意是给定一个质数,然后根据质数求出在该n数的组合排列中，每个质数都位于质数的位置
"""

Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
"""

import bisect
import math


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime = [True for _ in range(n + 1)]
        p = 2
        while p * p <= n:
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        primes = sum(prime[2:])
        return math.factorial(primes) * math.factorial(n - primes) % (10 ** 9 + 7)


#python的小技巧
class Solution2:
    def numPrimeArrangements(self, n: int) -> int:
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        cnt = bisect.bisect(primes, n)
        return math.factorial(cnt) * math.factorial(n - cnt) % (10 ** 9 + 7)