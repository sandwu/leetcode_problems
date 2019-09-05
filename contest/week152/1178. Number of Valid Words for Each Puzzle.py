


"""
题目相对好理解，给定两个列表puzzles和words，求满足两个条件的各有多少个：
    1.word contains the first letter of puzzle.
    2.For each letter in word, that letter is in puzzle.

"""

class Solution(object):
    """
    简单粗暴遍历，果断超时
    """
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        res = []
        for puzzle in puzzles:
            index = 0
            for word in words:
                if puzzle[0] in word:
                    flag = 1
                    for i in word:
                        if i not in set(puzzle):
                            flag = 0
                            break
                    if flag:
                        index += 1
            res.append(index)
        return res



class Solution2(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        count = collections.Counter(frozenset(w) for w in words)
        res = []
        for p in puzzles:
            subs = [p[0]]
            for c in p[1:]:
                subs += [s + c for s in subs]
            res.append(sum(count[frozenset(s)] for s in subs))
        return res