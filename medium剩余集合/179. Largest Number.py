



class Solution:
    """
    题意是给定一个集合nums，求里面的所有数字拼接的最大数字
    这里利用cmp_func来判断两个数组合哪个更大，比如3和30，330要大于303
    Runtime: 48 ms, faster than 59.44% of Python3 online submissions for Largest Number.
    Memory Usage: 14 MB, less than 7.14% of Python3 online submissions for Largest Number.
    """
    def largestNumber(self, nums) -> str:
        from functools import cmp_to_key
        def cmp_func(x, y):
            """Sorted by value of concatenated string increasingly."""
            if x + y > y + x:
                return 1
            elif x == y:
                return 0
            else:
                return -1

        # Build nums contains all numbers in the String format.
        nums = [str(num) for num in nums]

        # Sort nums by cmp_func decreasingly.
        nums.sort(key = cmp_to_key(cmp_func), reverse = True)

        # Remove leading 0s, if empty return '0'.
        return ''.join(nums).lstrip('0') or '0'

a = Solution()
nums = [3,30,34,5,9]
print(a.largestNumber(nums))