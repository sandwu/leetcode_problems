class Solution:
    """
    本题和26相像，因为空间复杂度都需求1，所以就只能在列表空间中进行更改；
    考虑到列表是可变的，每删除一个元素会使循环中的索引变更，所以每删除一个就continue跳过来避免。
    Runtime: 20 ms, faster than 100.00% of Python online submissions for Remove Element.
    """
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return None
        index = 0
        while index < len(nums):
            if nums[index] == val:
                del nums[index]
                continue
            index += 1
        return index

