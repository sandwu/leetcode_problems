
class MySolution:
    """
    先投机取巧用python的计数器counter来做，通过most_common去到值最多的1个[()]，然后通过索引定位到元素
    Runtime: 48 ms, faster than 94.33% of Python3 online submissions for Majority Element.
    """
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        c = Counter(nums)
        return c.most_common(1)[0][0]

class MySolution2:
    """
    这是除了Counter外自己想的比较笨拙的方法，通过字典存在就给值+1的方法来捕获，然后判断值是否大于n/2就ok了
    Runtime: 60 ms, faster than 59.69% of Python3 online submissions for Majority Element.
    """
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        res_dict = {}
        for i in nums:
            if i in res_dict:
                res_dict[i] += 1
                if res_dict[i] > len(nums)//2:
                    return i
            else:
                res_dict[i] = 1