
"""
Write a program to find the n-th ugly number.

Ugly numbers are positive integers which are divisible by a or b or c.



Example 1:

Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
Example 2:

Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 12... The 4th is 6.
Example 3:

Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
Example 4:

Input: n = 1000000000, a = 2, b = 217983653, c = 336916467

"""


class Solution:
    """
    二分+容斥
    容斥：在计数时，必须注意没有重复，没有遗漏。为了使重叠部分不被重复计算，人们研究出一种新的计数方法，
    这种方法的基本思想是：先不考虑重叠的情况，把包含于某内容中的所有对象的数目先计算出来，
    然后再把计数时重复计算的数目排斥出去，使得计算的结果既无遗漏又无重复，这种计数的方法称为容斥原理。
    简单说就是ABC三个集合，求其不重复的集合，即：（A∪B∪C = A+B+C - A∩B - B∩C - C∩A + A∩B∩C）
    """
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        import math
        def lcm(a, b):
            return abs(a*b) // math.gcd(a, b)
        def count(val,a,b,c):
            return val//a + val//b + val//c -val//lcm(a, b)-val//lcm(a, c)-val//lcm(c, b) + val//lcm(lcm(a, b),c)
        l = 1
        r = min([a,b,c]) * n
        tmp = (l+r)//2
        while count(tmp,a,b,c) != n-1:
            if count(tmp,a,b,c) > n-1:
                r = tmp
            else:
                l = tmp
            tmp = (l+r)//2
        while count(tmp,a,b,c) != n:
            tmp += 1
        return tmp