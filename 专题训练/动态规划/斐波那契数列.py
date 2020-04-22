

#leetcode 70爬楼梯

class Solution:
    def fibonaci(self,n):#直接递归求解
        if n==1:return 1
        if n==2:return 2
        return self.fibonaci(n-1) + self.fibonaci(n-2)

    def fibonaci2(self,n,tmp={}): #加上备忘录
        if n==1:return 1
        if n==2:return 2
        if tmp.get(n):
            return tmp[n]
        val = self.fibonaci(n-1) + self.fibonaci(n-2)
        tmp[n] = val
        return val

    def fibonaci3(self,n): #dp
        if n==1:return 1
        if n==2:return 2
        pre,next,res = 1,2,0
        for _ in range(3,n+1):
            res = pre+next
            pre,next = next,res
        return res


class Solution2(object):
    """
    Time Limit Exceeded
    """
    def climbStairs(self, n):
        """
        time
        :type n: int
        :rtype: int
        """
        if n==1:return 1
        if n==2:return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

class Solution3(object):
    """
    Runtime: 20 ms, faster than 40.97% of Python online submissions for Climbing Stairs.
    Memory Usage: 11.9 MB, less than 9.38% of Python online submissions for Climbing Stairs.
    """
    def climbStairs(self, n, tmp={}):
        """
        :type n: int
        :rtype: int
        """
        if n==1:return 1
        if n==2:return 2
        if tmp.get(n):
            return tmp[n]
        val = self.climbStairs(n-1) + self.climbStairs(n-2)
        tmp[n] = val
        return val

class Solution4(object):
    """
    Runtime: 16 ms, faster than 69.96% of Python online submissions for Climbing Stairs.
    Memory Usage: 11.9 MB, less than 15.63% of Python online submissions for Climbing Stairs.
    """
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:return 1
        if n==2:return 2
        pre,next,res = 1,2,0
        for _ in range(3,n+1):
            res = pre+next
            pre,next = next,res
        return res



a = Solution()
print(a.fibonaci(10))
print(a.fibonaci2(10))
print(a.fibonaci3(10))




