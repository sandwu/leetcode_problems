
"""

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit = [0] * 32
        for num in nums:
            for i in range(32):
                bit[i] += num >> i & 1
        res = 0
        for i, val in enumerate(bit):
            # if the single numble is negative,
            # this case should be considered separately
            if i == 31 and val%3:
                res = -((1<<31)-res)
            else:
                res |= (val%3)*(1<<i)
        return res


class Solution1(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            cnt = 0
            mask = 1 << i
            for num in nums:
                if num & mask:
                    cnt += 1
            if cnt % 3 == 1:
                res |= mask
        if res >= 2 ** 31:
            res -= 2 ** 32
        return res


class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def num2bin(num):
            i = 0
            if num < 0:
                num = -num
                count[32] += 1
            while num > 0:
                num, r = divmod(num, 2)
                count[i] += r
                i += 1

        def bin2num(binary):
            mult = 1
            ans = 0
            for i in range(len(binary) - 1):
                ans += mult * binary[i]
                mult *= 2
            return ans

        count = [0] * 33
        for n in nums:
            num2bin(n)
        for i in range(len(count)):
            count[i] %= 3
        res = bin2num(count)
        return res if count[-1] == 0 else -res