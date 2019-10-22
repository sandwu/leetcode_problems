



class Solution(object):
    """
    题意是求一组数中的两个不重复的值，要求时间O(n)空间O(1)，这里取巧用空间和时间都是O(1)
    Runtime: 40 ms, faster than 91.15% of Python online submissions for Single Number III.
    Memory Usage: 13.8 MB, less than 50.00% of Python online submissions for Single Number III.
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pairs = set()
        for n in nums:
            if n in pairs:
                pairs.remove(n)
            else:
                pairs.add(n)
        return list(pairs)


class Solution2(object):
    """
    字典的方式处理，空间仍旧是O(n)
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic, res = {}, []
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for k, v in dic.items():
            if v == 1:
                res.append(k)
        return res

class Solution3(object):
    """
    用位运算还是最准的，空间O(1)
    Runtime: 40 ms, faster than 91.15% of Python online submissions for Single Number III.
    Memory Usage: 13.2 MB, less than 75.00% of Python online submissions for Single Number III.
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # "xor" all the nums
        tmp = 0
        for num in nums:
            tmp ^= num
        # find the rightmost "1" bit
        i = 0
        while tmp & 1 == 0:
            tmp >>= 1
            i += 1
        tmp = 1 << i
        # compute in two seperate groups
        first, second = 0, 0
        for num in nums:
            if num & tmp:
                first ^= num
            else:
                second ^= num
        return [first, second]