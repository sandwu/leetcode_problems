

class Solution(object):
    """
    需要遍历两次，效率上变低，不过通过字典来完成是最快想到的方式
    Runtime: 96 ms, faster than 32.54% of Python online submissions for Single Number.
    Memory Usage: 15 MB, less than 5.11% of Python online submissions for Single Number.
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0) + 1
        for key,val in dic.items():
            if val == 1:
                return key


class Solution2(object):
    """
    用二进制的异或来完成也是很巧妙，异或是比较两者的二进制数，按位运算，当两者不同时，返回0；相同时返回1，
    所以直接遍历，取第一个值0，0和任何值得异或都是其本身，接下来不同值一直累加，碰到相同的就返回1，知道找到
    最后一个不同的。
    Runtime: 72 ms, faster than 40.33% of Python online submissions for Single Number.
    Memory Usage: 13.7 MB, less than 5.11% of Python online submissions for Single Number.
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res



class Solution3(object):
    """
    通过sum求和来做
    Runtime: 68 ms, faster than 41.18% of Python online submissions for Single Number.
    Memory Usage: 13.8 MB, less than 5.11% of Python online submissions for Single Number.
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2*sum(set(nums))-sum(nums)