

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        rec = set(nums)
        if len(nums) != len(rec):return True
        else:return False