

class Solution(object):
    """
    利用for+递归来实现，针对序列里的每个数，递归找到所有组合；而针对序列的每个数再做判断，如果相似就跳过
    Runtime: 28 ms, faster than 100.00% of Python online submissions for Subsets II.
    Memory Usage: 10.9 MB, less than 65.26% of Python online submissions for Subsets II.
    """
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, path+[nums[i]], res)




class Solution2(object):
    """
    Use a dictionary to keep track of the number of appearances of each number. One can then easily construct the power set of nums based on this dictionary.

    E.g., nums = [1,1,2,2,2,4,4,5]. In this case dic = {1:2, 2:3, 4:2, 5:1}. We intialize res = [[]], and build the solution iteratively as we loop over the dictionary. We first reach key, val = 1, 2. The power set of [1,1] is res = [[], [1], [1,1]]. Then we reach key, val = 2, 3. The power set of [1,1,2,2,2] is obtained by appending either 0, 1, 2, or 3 2's to all elements in res. After which we get res = [[], [1], [1,1], [2], [1,2], [1,1,2],[2,2], [1,2,2], [1,1,2,2],[2,2,2], [1,2,2,2], [1,1,2,2,2]]. After we loop over dic, res will be the power set of nums.

    Time complexity: O(2^n), space complexity: O(2^n).
    Runtime: 32 ms, faster than 91.48% of Python online submissions for Subsets II.
    Memory Usage: 10.7 MB, less than 100.00% of Python online submissions for Subsets II.
    """
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        res = [[]]
        dic = collections.Counter(nums)
        for key, val in dic.items():
            tmp = []
            for lst in res:
                for i in range(1, val+1):
                    tmp.append(lst+[key]*i)
            res += tmp
        return res