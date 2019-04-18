

class Solution(object):
    """
    set来做简直不要太轻松
    Runtime: 108 ms, faster than 39.28% of Python online submissions for Contains Duplicate.
    Memory Usage: 17.3 MB, less than 5.24% of Python online submissions for Contains Duplicate.
    """
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)


class Solution2(object):
    """
    也可以用字典或者集合
    Runtime: 112 ms, faster than 35.03% of Python online submissions for Contains Duplicate.
    Memory Usage: 17.1 MB, less than 5.24% of Python online submissions for Contains Duplicate.
    """
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for index,val in enumerate(nums):
            if val in dic:
                return True
            else:
                dic[val] = index
        return False