class Solution(object):
    """
    讨论区真的是大神云集，这个思路是真的强，首尾的1直接利用zip里的两个列表首尾增加[0]来完成，因为每行的上一行一定是首尾为1。
    接下来就是简单的两两相加和，是真的厉害！完成度也是达到了100%
    Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Pascal's Triangle II.
    """
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row


class Solution2:
    “”“
    利用两次遍历，是通俗能想得到的方法，首先构造需要求的列表，用1填充，然后跟杨辉三角1的解决方案一样，第一次遍历行，第二次遍历列， 直到结束，返回对应的行。
    Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Pascal's Triangle II.
    ”“”
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]*(rowIndex+1)
        for i in range(2, rowIndex+1):
            prev = res[0]
            for j in range(1,i):
                tmp = res[j]
                res[j] = prev+res[j]
                prev = tmp
        return res