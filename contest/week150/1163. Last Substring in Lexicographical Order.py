

# 题目是求字符串里的最大字典序

class Solution:
    def lastSubstring(self, s: str) -> str:
        if len(set(s)) == 1: return s
        idx = len(s) - 1
        for i in range(len(s)-2, -1, -1):
            k = 0
            while idx+k < len(s):
                cur, stored = ord(s[i+k]), ord(s[idx+k])
                if cur > stored:
                    idx = i
                    break
                elif cur < stored:
                    break
                k += 1
            if idx+k == len(s):
                idx = i
        return s[idx:]