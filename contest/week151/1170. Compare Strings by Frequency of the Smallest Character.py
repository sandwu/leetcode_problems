from _bisect import bisect
from collections import Counter


class Solution(object):
    """
    题意是比对两个列表集合，其中最小字母的出现次数！然后依次填出第二个集合比第1个集合高的次数的个数
    解法：针对每个集合求出对应的数字和，然后遍历第1、第2个集合，得出答案
    """
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        for i in range(len(queries)):
            nums = self.get_nums(queries[i])
            queries[i] = nums

        for j in range(len(words)):
            nums = self.get_nums(words[j])
            words[j] = nums

        for query in queries:
            index = 0
            for word in words:
                if query < word:
                    index += 1
            res.append(index)
        return res

    def get_nums(self, word):
        dict1 = {}
        for i in word:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        min_alp = min(list(dict1.keys()))
        return dict1[min_alp]

class Solution1(object):
    """
    上述算法的简化版
    """
    def numSmallerByFrequency(self, queries, words):
        freq, ans = [], []
        for word in words:
            c = Counter(word)
            freq.append(c[min(c.keys())])
        freq.sort()
        n = len(freq)
        for query in queries:
            c = Counter(query)
            ans.append(n - bisect(freq, c[min(c.keys())]))
        return ans

a = Solution()
q = ["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"]
w = ["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"]
print(a.numSmallerByFrequency(q,w))