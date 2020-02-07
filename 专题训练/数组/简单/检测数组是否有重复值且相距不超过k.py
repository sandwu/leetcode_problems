

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic1 = {}
        for i,v in enumerate(nums):
            if v in dic1 and i - dic1[v] <= k:
                return True
            dic1[v] = i
        return False