
class Solution(object):
    """
    解题的思路就是定义nums[:j]存放的是0，nums[k:]存放的是2，这样剩余中间的即是1
    代码是用快慢两个指针，也就是i，j，当j碰到0就和i调换，即使此时的nums[i]是不是0，调换后i+1，然后j会再做一次判断
    同理的nums[j]==2也是这样处理
    Runtime: 20 ms, faster than 98.75% of Python online submissions for Sort Colors.
    Memory Usage: 10.8 MB, less than 40.74% of Python online submissions for Sort Colors.
    """
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        k = len(nums)-1
        j = i
        while j <= k:
            if i < j and nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            elif nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1


class Solution2(object):
    """
    这个解法太强了，因为题目的限制是原地变动，基本就没想过用额外空间的方法，而下述代码则直接绕过创空间来实现
    Runtime: 20 ms, faster than 98.75% of Python online submissions for Sort Colors.
    Memory Usage: 10.6 MB, less than 90.57% of Python online submissions for Sort Colors.
    """
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c0 = c1 = c2 = 0
        for num in nums:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1
        nums[:c0] = [0] * c0
        nums[c0:c1+c1] = [1] * c1
        nums[c0+c1:] = [2] * c2