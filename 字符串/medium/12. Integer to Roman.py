

class Solution(object):
    """
    讨论区最佳，感觉有点投机取巧，将4、9这种特殊的情况都列到列表里去即可了
    Runtime: 52 ms, faster than 97.22% of Python online submissions for Integer to Roman.
    Memory Usage: 11.8 MB, less than 5.76% of Python online submissions for Integer to Roman.
    """
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res, i = "", 0
        while num:
            res += (num // values[i]) * numerals[i]
            num %= values[i]
            i += 1
        return res
