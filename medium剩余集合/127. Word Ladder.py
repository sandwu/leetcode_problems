import collections


class Solution(object):
    """
    题意是求给两个单词begin、end和一个列表，从begin转换为end，要经历多少步骤，每次转换的单词都必须在列表
    并且单词一次只能转换一个字母
    解法：bfs，借鉴：https://blog.csdn.net/fuxuemingzhu/article/details/82903681
    可以参考迷宫的解法，每次将所有可能结果都加入queue里，每加入一个，对应的length上就+1，知道end找到就返回length
    Runtime: 420 ms, faster than 37.93% of Python online submissions for Word Ladder.
    Memory Usage: 13 MB, less than 67.57% of Python online submissions for Word Ladder.
    """
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0