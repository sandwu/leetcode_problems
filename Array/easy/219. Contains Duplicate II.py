
class MySolution:
    """
    我的解法还是利用字典来做，要注意的是当第一轮找到的两个相同的数距离大于k时，要用第二个数的index重置第一个数，继续往下遍历
    Runtime: 48 ms, faster than 88.89% of Python3 online submissions for Contains Duplicate II.
    """
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        res_dict = {}
        for index,value in enumerate(nums):
            if value not in res_dict:
                res_dict[value] = index
            else:
                res = index - res_dict[value]
                if res <= k:
                    return True
                else:
                    res_dict[value] = index
        return False

class Solution:
    """
    看到讨论区的字典解法比我的简单点，不过原理是一样的，mark一下，不过连runtime都比我的好
    Runtime: 44 ms, faster than 97.62% of Python3 online submissions for Contains Duplicate II.
    """
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False