class Solution(object):
    """
    这道题光是题目就难倒了我，简单查了下，原来是找列表的所有排列情况，并且第一行默认是asc排序，最后一行是desc，依次排列出所有情况，
    然后给出任一行，推测出它的下一行，比如[1,2,3]就有以下情况：
    1 2 3
    1 3 2
    2 1 3
    2 3 1
    3 1 2
    3 2 1
    我个人是想了非常多的if..else..，结果提交时还是各种各样的错，最后看了网上答案，原来就是将数学规律写成代码；
    数学规律：6 5 4 8 7 3 1
    以上面为例，从后往前看，依次递增，直到4的时候结束，那么此时找出从4之后的所有数里比4大的最小数，交换他们，然后升序排序索引2(也就是原来4)
    仔细看代码，就是完完整整依据上面的逻辑，不过为了方便，是先将4之后的排序，再交换位置，道理是一样的。
    至于如何推导的，我是推导了下，不过比较麻烦，就不多说了，大家可以借助我函数里的三种情况进行推导，就是从后往前，判断每种情况下的变化
    Runtime: 28 ms, faster than 100.00% of Python online submissions for Next Permutation.
    Memory Usage: 10.8 MB, less than 100.00% of Python online submissions for Next Permutation.    
    """
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        6 5 4 1 3 7 8 
        6 5 4 1 7 8 3
        6 5 4 8 7 3 1
        """
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        self.reverse(nums, i, n - 1)
        if i > 0:
            for j in range(i, n):
                if nums[j] > nums[i-1]:
                    self.swap(nums, i-1, j)
                    break
        
    def reverse(self, nums, i, j):
        """
        contains i and j.
        """
        for k in range(i, (i + j) / 2 + 1):
            self.swap(nums, k, i + j - k)

        
    def swap(self, nums, i, j):
        """
        contains i and j.
        """
        nums[i], nums[j] = nums[j], nums[i]