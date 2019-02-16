class MySolution:
    """
    利用enumerate获取列表的下标和值，将值作为key，下标作为value存入字典，只需O(n)的时间复杂度
    Runtime: 36 ms, faster than 99.77% of Python3 online submissions for Two Sum.
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        for i, v in enumerate(nums):
            sub = target - v
            if sub in dict1:
                return [dict1[sub], i]
            else:
                dict1[v] = i


class Solution:
    """
    讨论区解法，利用遍历来查找是否存在，要注意的是用index找不到则会报错，所以用try、except；另外index可以跟上第二参数是起始点
    Runtime: 36 ms, faster than 99.77% of Python3 online submissions for Two Sum.
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = set(nums)
        for i in range(len(nums)-1):
            if target-nums[i] in s:
                try:
                    res = nums.index(target-nums[i], i+1)
                    break
                except:
                    continue
        return (i,res)