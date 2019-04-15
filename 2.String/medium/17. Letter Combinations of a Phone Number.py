
class Solution(object):
    """
    可以不断拆解的问题：如果是8位数，肯定是前7位数的组合和最后一位数的组合，如果是7位数，就是前6位的组合和
    最后一位的组合，依次类推，直到第一位，返回字典里对应的集合即可
    Runtime: 20 ms, faster than 74.78% of Python online submissions for Letter Combinations of a Phone Number.
    Memory Usage: 11.7 MB, less than 5.15% of Python online submissions for Letter Combinations of a Phone Number.
    """
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        addt = list(mapping[digits[-1]])
        return [a + c for a in prev for c in addt]