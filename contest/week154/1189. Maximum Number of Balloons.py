
"""

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
"""
from future.moves import collections


class Solution:
    """
    我一直卡在如何构建balloon的字典，因为balloon是一个有重复值的str，解法直接构建一个text的字典，通过不断比对
    balloon和text字典的差异，每完成一次则+1
    """
    def maxNumberOfBalloons(self, text: str) -> int:
        d, count = {}, 0
        for l in text:
            if l in d: d[l] += 1
            else: d[l] = 1

        while True:
            a = ['b' ,'a', 'l', 'l', 'o', 'o', 'n']
            for i in range(len(a)):
                if a[i] in d and d[a[i]] > 0:
                    d[a[i]] -= 1
                    a[i] = ''
            if a == [''] * 7: count += 1
            else: break

        return count

class Solution2:
    """
    上面方法的简写
    """
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = collections.Counter(text)
        cntBalloon = collections.Counter('balloon')
        return min([cnt[c] // cntBalloon[c] for c in 'balloon'])