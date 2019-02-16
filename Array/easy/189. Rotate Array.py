
class MySolution:
    """
    我的解决方法就是通常想到的，通过循环，每一次把最后的数插入到最前方。当然效率也是很慢的，达到132ms
    Runtime: 132 ms, faster than 22.71% of Python3 online submissions for Rotate Array.
    """
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = -1
        while index >= -k:
            nums.insert(0, nums.pop())
            index -= 1

class Solution:
    """
    讨论区看的答案，还是被惊艳到了，直接对nums进行三次颠倒就行了，相当于从宏观来考虑
    不过需要补上k取余，因为会给出k的值大于nums的length情况
    Runtime: 44 ms, faster than 100.00% of Python3 online submissions for Rotate Array.
    """
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:-k] = nums[:-k][::-1]
        nums[-k:] = nums[-k:][::-1]
        nums[:] = nums[::-1]

class Solution2:
    """
    可以在上述方法再做优化，直接取一半的数值
    """
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[n-k:] + nums[:n-k]