

class Solution(object):
    """
    除了用stack来完成，这里的判断还是比较有技巧的，
    1.显示通过num*10来判断当数字超过2个以上时的状态，如果碰到符号就重置num=0
    2.判断除法，因为-5//2=-3，所以要+1，
    Runtime: 104 ms, faster than 86.79% of Python online submissions for Basic Calculator II.
    Memory Usage: 20.9 MB, less than 10.57% of Python online submissions for Basic Calculator II.
    """
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return "0"
        stack,num,sign = [],0,"+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord("0")
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    tmp = stack.pop()
                    if tmp/num<0 and tmp%num !=0:
                        stack.append(tmp//num +1)
                    else:
                        stack.append(tmp//num)
                sign = s[i]
                num = 0
        return sum(stack)