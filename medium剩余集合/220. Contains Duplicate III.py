



class Solution(object):
    """
    桶排序来实现
    Runtime: 44 ms, faster than 70.84% of Python online submissions for Contains Duplicate III.
    Memory Usage: 13.8 MB, less than 100.00% of Python online submissions for Contains Duplicate III.
    """
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False
        cache = {}
        for i in range(len(nums)):
            if i-k > 0:
                bucket_id_to_delete = nums[i-k-1]//(t+1)
                del cache[bucket_id_to_delete]
            bucket_id = nums[i]//(t+1)
            condition1 = (bucket_id in cache)
            condition2 = ((bucket_id-1 in cache and abs(cache[bucket_id-1]-nums[i])<= t))
            condition3 = ((bucket_id+1 in cache and abs(cache[bucket_id+1]-nums[i])<= t))
            if condition1 or condition2 or condition3:
                return True
            cache[bucket_id] = nums[i]
        return False