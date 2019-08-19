


class Solution:
    """
    题意是求给定集合里的数是否都在chars里面，每个数只能用一次
    解法：即暴力循环，每次判断集合里数是否存在，存在就删除，不存在就说明不符合，直到遍历完
    """
    def countCharacters(self, words, chars: str) -> int:
        res = ""
        for word in words:
            flag = 0
            strs = chars
            for alp in word:
                if alp not in strs:
                    flag = 1
                    break
                else:
                    strs = strs.replace(alp,'',1)
            if flag == 0:res += word
        return len(res)

l = ["hello","world","leetcode"]
s = "welldonehoneyr"
a = Solution()
print(a.countCharacters(l, s))