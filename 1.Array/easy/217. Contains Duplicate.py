
class MySolution:
    """
    我的解法很简单，还是从字典入手，如果发现当前值存在字典，则说明超过两次；当然速度就堪忧了。
    Runtime: 48 ms, faster than 80.28% of Python3 online submissions for Contains Duplicate.
    """
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res_dict = {}
        for i in nums:
            if i not in res_dict:
                res_dict[i] = 0
            else:
                return True
        return False

class MySolution2:
    """
    看到数数就想到python的计数器，我的第二种解法就是利用Counter和它most_common来做
    Runtime: 48 ms, faster than 80.28% of Python3 online submissions for Contains Duplicate.
    """
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter
        if not len(nums):
            return False
        c = Counter(nums)
        res = c.most_common(1)[0][1]
        return res != 1

class Solution:
    """
    讨论区的一向精简，直接通过set来完成，不得不说从列表中判断数量时set非常好用
    Runtime: 44 ms, faster than 98.12% of Python3 online submissions for Contains Duplicate.
    """
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)