import heapq


class Solution(object):
    """
    题目是取第k大的数字，直接取巧排序后取值
    Runtime: 52 ms, faster than 75.57% of Python online submissions for Kth Largest Element in an Array.
    Memory Usage: 12.3 MB, less than 64.15% of Python online submissions for Kth Largest Element in an Array.
    """
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        return nums[k-1]

    def findKthLargestHeap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        new_nums = [-1 * n for n in nums]
        heapq.heapify(new_nums)
        while k > 1:
            heapq.heappop(new_nums)
            k -= 1
        return -new_nums[0]

    def findKthLargestPartition(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start, end, rank = 0, len(nums) - 1, len(nums) - (k - 1)
        # random.shuffle(nums)
        while start <= end:
            ret = self._partition(nums, start, end)
            if ret == rank - 1:
                return nums[ret]
            elif ret < rank - 1:
                start = ret + 1
            else:
                end = ret - 1

    def _partition(self, nums, start, end):
        pivot = start

        while start < end:
            while nums[end] > nums[pivot] and end > start:
                end -= 1
            while nums[start] <= nums[pivot] and start < end:
                start += 1

            nums[start], nums[end] = nums[end], nums[start]

        nums[pivot], nums[start] = nums[start], nums[pivot]

        return start