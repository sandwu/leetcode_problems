class Solution:
    """
    第一反应就是用合并排序来做，但合并排序是新建列表，而题目要求是在nums1上原地改动，思路和合并排序是一致的，参照讨论区的解如下
    效率：Runtime: 56 ms, faster than 96.65% of Python3 online submissions for Merge Sorted Array.
    """
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        
        while i >= 0:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

class Solution2:
    “”“
    简化版，看的非常的舒服；从最后一个数开始比较，就能避免nums1填充的0的阻碍
    效率：Runtime: 56 ms, faster than 96.65% of Python3 online submissions for Merge Sorted Array.
    ”“”
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]