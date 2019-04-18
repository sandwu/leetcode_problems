

class Solution(object):
    """
    跟217一致，通过dict来记录过往历史即可
    Runtime: 80 ms, faster than 36.08% of Python online submissions for Contains Duplicate II.
    Memory Usage: 16.2 MB, less than 8.34% of Python online submissions for Contains Duplicate II.
    """
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for index,val in enumerate(nums):
            if val in dic:
                if  index - dic[val] <= k:
                    return True
                else:
                    dic[val] = index
            else:
                dic[val] = index
        return False