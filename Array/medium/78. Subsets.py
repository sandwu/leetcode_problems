

class Solution(object):
    """
    迭代解法：代码的实现真的很巧妙，结合规律，以题目为例：
    [1,2,3]答案里：[]
                  [1],[1,2],[1,3],[1,2,3]
                  [2],[2,3]
                  [3]
    即每遍历一个数，新加入[]+[num];然后再在已拥有的集合里增加新的数，比如3，已有的集合就是：[1],[1,2],[2],
    依次转换为[1,3],[1,2,3],[2,3]
    Runtime: 24 ms, faster than 100.00% of Python online submissions for Subsets.
    Memory Usage: 11 MB, less than 37.77% of Python online submissions for Subsets.
    """
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            for i in range(len(res)):
                res.append(res[i]+[num])
        return res

class Solution2(object):
    """
    递归解法：原理和迭代是一致的，但因为是递归，所以理解起来稍微费脑
    该解法从最后一次递归返回结果开始，然后跟迭代一致的想法，在上一个结果的基础上，依次增加当前数；
    以[1,2,3]为例，第一次递归返回：[],[3]，此时的head为2，所以for遍历后结果为：[],[3],[2],[3,2]
    接着得到的res再次返回，此时head为1，所以再依次加上得：[1],[3,1],[2,1],[3,2,1]
    Runtime: 24 ms, faster than 100.00% of Python online submissions for Subsets.
    Memory Usage: 11 MB, less than 50.82% of Python online submissions for Subsets.
    """
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def helper(nums, i, j):
            if i > j:
                return [[]]
            if j - i == 1:
                return [[], [nums[i]]]
            head = nums[i]
            res = helper(nums, i + 1, j)
            for i in range(len(res)):
                res.append(res[i] + [head])
            return res

        return helper(nums, 0, len(nums))