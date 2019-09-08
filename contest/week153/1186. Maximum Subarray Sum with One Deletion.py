

"""
题意是给个非空数组，然后求最大子集，不过可以将子集中的任意一个数去掉

"""

"""

解法，看到这题就想到动态规划解决Maximum Subarray Sum的答案，所以解法就是改编版如下
"""

class Solution(object):
    """
    要设定两个list，前者用来不改变删除值的每一个数值(因为一次只能删除一个)
    后者则用来保存删除后的最大值
    """
    def maximumSum(self, arr) -> int:
        n = len(arr)
        max_ending_here0 = n * [arr[0]]
        max_ending_here1 = n * [arr[0]]
        for i in range(1, n):
            max_ending_here0[i] = max(max_ending_here0[i - 1] + arr[i], arr[i])
            max_ending_here1[i] = max(max_ending_here1[i - 1] + arr[i], arr[i])
            if i >= 2:
                max_ending_here1[i] = max(max_ending_here1[i], max_ending_here0[i - 2] + arr[i])
        return max(max_ending_here1)



#动态规划解决Maximum Subarray Sum

def maximumSum(self, arr: List[int]) -> int:
    n = len(arr)
    max_ending_here = n * [arr[0]]
    for i in range(1, n):
        max_ending_here[i] = max(max_ending_here[i-1] + arr[i], arr[i])
    return max(max_ending_here)