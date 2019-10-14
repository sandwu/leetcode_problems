
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class WordDictionary(object):
    """
    Runtime: 420 ms, faster than 33.85% of Python online submissions for Add and Search Word - Data structure design.
Memory Usage: 36.3 MB, less than 7.14% of Python online submissions for Add and Search Word - Data structure design.
    """
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res

    def dfs(self, node, word):
        if not word:
            if node.isWord:
                self.res = True
            return
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])