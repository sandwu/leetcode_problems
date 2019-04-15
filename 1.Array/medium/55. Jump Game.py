
class Solution:
    """
    贪心算法，每一步都算上一个数的索引和它的值的和是否有能力到达这一个数，如果可以的话，则说明有能力到达最后一个数，
    不行的话就直接返回False
    Runtime: 48 ms, faster than 73.92% of Python3 online submissions for Jump Game.
    Memory Usage: 14.7 MB, less than 5.28% of Python3 online submissions for Jump Game.
    """
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)):
            if i > reach:
                return False
            reach = max(reach, i+nums[i])
        return True