


class Solution(object):
    """
    用传统的dict来完成，不在时加入，在时进行判断：首先判断是否当前的下标差为最大值，接着需要判断下标的起始点更新，
    比如'abcdbce'，前四个正常录入dict，而到了下标4也就是'b'时，因为'b'在dict里面，所以start从0变成2也就是'c'的位置，
    因为接下来不重复的肯定是从c开始计数了，直到又碰到c，此时下标就从2变成6，for也循环结束了，然后返回最大值
    Runtime: 80 ms, faster than 37.09% of Python online submissions for Longest Substring Without Repeating Characters.
    Memory Usage: 12.3 MB, less than 9.40% of Python online submissions for Longest Substring Without Repeating Characters.
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                # update the res
                res = max(res, i-start)
                # here should be careful, like "abba"
                start = max(start, dic[ch]+1)
            dic[ch] = i
        # return should consider the last
        # non-repeated substring
        return max(res, len(s)-start)