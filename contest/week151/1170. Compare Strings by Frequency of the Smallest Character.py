
class Solution(object):
    """


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

a = Solution()
q = ["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"]
w = ["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"]
print(a.numSmallerByFrequency(q,w))