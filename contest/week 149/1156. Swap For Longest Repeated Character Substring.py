import collections
import itertools


class Solution:
    """
    题意是求给定字符串，调换位置，使得连续子集最大
    仅2种情况：1.直接在最大的子字符集+1 2.两个子字符集中夹杂1个其余字符集，更换这个其余的字符集即可
    """
    def maxRepOpt1(self, text: str) -> int:
        # We get the group's key and length first, e.g. 'aaabaaa' -> [[a , 3], [b, 1], [a, 3]
        A = [[c, len(list(g))] for c, g in itertools.groupby(text)]
        # We also generate a count dict for easy look up e.g. 'aaabaaa' -> {a: 6, b: 1}
        count = collections.Counter(text)
        # only extend 1 more, use min here to avoid the case that there's no extra char to extend
        res = max(min(k + 1, count[c]) for c, k in A)
        # merge 2 groups together
        for i in range(1, len(A) - 1):
            # if both sides have the same char and are separated by only 1 char
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                # min here serves the same purpose
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))
        return res