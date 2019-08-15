import bisect
import collections
import random


#https://leetcode.com/problems/online-majority-element-in-subarray/discuss/355848/Python-Binary-Search-%2B-Find-the-Majority-Element

class MajorityChecker:

    def __init__(self, A):
        a2i = collections.defaultdict(list)
        for i, x in enumerate(A):
            a2i[x].append(i)
        self.A, self.a2i = A, a2i

    def query(self, left, right, threshold):
        for _ in range(10):
            a = self.A[random.randint(left, right)]
            l = bisect.bisect_left(self.a2i[a], left)
            r = bisect.bisect_right(self.a2i[a], right)
            if r - l >= threshold:
                return a
        return -1