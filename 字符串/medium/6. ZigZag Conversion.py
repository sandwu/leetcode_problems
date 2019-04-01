

class Solution(object):
    """
    该解法厉害的地方就在于对于换行取模的判断，首先看清题意，以4行为例，第一列全齐，第二列仅倒数第二个，第三列倒数第三个，
    第四列又齐，所以这边取模就能看到，line=0、4、8满足条件，对应的在4，8开始回滚-1.
    Runtime: 48 ms, faster than 99.93% of Python online submissions for ZigZag Conversion.
    Memory Usage: 12 MB, less than 11.06% of Python online submissions for ZigZag Conversion.
    """
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or numRows >= len(s):
            return s
        arr = [''] * numRows
        line, step = 0, -1
        for c in s:
            arr[line] += c
            if line % (numRows - 1) == 0:
                step = - step
            line += step
        return ''.join(arr)

