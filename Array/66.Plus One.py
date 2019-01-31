class MySolution:
    """
    思路很简单，如果是9就判断一下，如果不是就直接+1返回结果，要注意的是遍历完后如果第一位是0，则说明需要加1
    效率：Runtime: 56 ms, faster than 95.99% of Python3 online submissions for Plus One.
    """
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        for num in range(n-1,-1,-1):
            if  digits[num]== 9:
                digits[num] = 0
            else:
                digits[num] += 1
                break
        if digits[0] == 0:
            digits.insert(0,1)
        return digits


class Solution1:
    """
    讨论区递归思路，也是蛮好的；
    效率：Runtime: 56 ms, faster than 95.99% of Python3 online submissions for Plus One
    """
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        if digits[-1] != 9:
            return digits[0:n-1]+ [digits[-1]+1]
        elif n>1:
            return self.plusOne(digits[0:n-1]) + [0]
        else:
            return [1,0]

class Solution1:
    “”“
    利用转换的思想，先转换为int来计算，再转回table，也算是一种思路
    效率：Runtime: 56 ms, faster than 95.99% of Python3 online submissions for Plus One.
    ”“”
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp = ""
        for i in digits:
            temp += str(i)
        temp = int(temp)
        temp = temp + 1
        return [int(x) for x in str(temp)]