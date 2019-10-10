
class Trie(object):
    """
    Runtime: 116 ms, faster than 97.61% of Python online submissions for Implement Trie (Prefix Tree).
    Memory Usage: 27.8 MB, less than 94.12% of Python online submissions for Implement Trie (Prefix Tree).
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = '#'

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        t = self.trie
        for w in word:
            if w not in t:
                return False
            t = t[w]
        if '#' in t:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        t = self.trie
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)