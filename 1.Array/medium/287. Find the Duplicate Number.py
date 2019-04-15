
class Solution(object):
    """
    用Counter来做也是取巧了
    Runtime: 32 ms, faster than 46.18% of Python online submissions for Find the Duplicate Number.
    Memory Usage: 15.9 MB, less than 5.35% of Python online submissions for Find the Duplicate Number.
    """
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        c = Counter(nums)
        return c.most_common()[0][0]

class Solution2(object):
    """
    Solution用set来实现，也不算额外空间
    Runtime: 36 ms, faster than 38.09% of Python online submissions for Find the Duplicate Number.
    Memory Usage: 12.3 MB, less than 42.80% of Python online submissions for Find the Duplicate Number.
    """
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

class Solution3(object):
    """
    映射找环法，对每个下标和对应的值进行映射，然后不断重复过程，如果有相同的值，则他们的映射是相同的，
    此时就会陷入不断重复，这是第一个for；第二个for就是找到重复的第一个起始点。
    具体：https://segmentfault.com/a/1190000003817671
    Runtime: 20 ms, faster than 100.00% of Python online submissions for Find the Duplicate Number.
    Memory Usage: 12 MB, less than 54.32% of Python online submissions for Find the Duplicate Number.
    """
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow