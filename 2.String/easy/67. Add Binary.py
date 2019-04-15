
class Solution(object):
    """
    0b+'a' 获取二进制的值，比如0b11，通过eval获取字符串表达式的值为3,相加后再通过bin转为二进制；
    实际上等价于：bin(int(a, 2) + int(b, 2))[2:]
    Runtime: 24 ms, faster than 86.44% of Python online submissions for Add Binary.
    Memory Usage: 11.9 MB, less than 5.18% of Python online submissions for Add Binary.
    """
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(eval('0b'+a)+eval('0b'+b))[2:]
        # return bin(int(a, 2) + int(b, 2))[2:]


class Solution2(object):
    """
    感觉这才是标准不取巧解法，直接通过二进制位数相加判断获取结果，方法还是很巧妙，mark一下
    Runtime: 32 ms, faster than 44.25% of Python online submissions for Add Binary.
    Memory Usage: 12.1 MB, less than 5.18% of Python online submissions for Add Binary.
    """
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i,j,carry,res=len(a)-1,len(b)-1,0,''
        while i>=0 or j>=0 or carry > 0:
            if i>=0:
                carry += int(a[i])
                i -= 1
            if j>=0:
                carry += int(b[j])
                j-=1
            res = str(carry%2) + res
            carry //= 2
        return res