
class Solution1:
    """
    从首尾开始计算初步的最大值,然后从首尾短的那边开始往中间推移,不断地计算最大,直到中间汇合则break出来,有点类似于贪心算法,即一直取当前最大的面积.
    Runtime: 60 ms, faster than 79.17% of Python3 online submissions for Container With Most Water.
    """
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start,end,now_max = 0,len(height)-1,0
        while start < end:
            now_max = max(now_max, (end-start)*min(height[start], height[end]))
            if height[end] < height[start]:
                end -= 1
            else:
                start += 1
        return now_max



class Solution:
    """
    讨论区的解法,时间复杂度要优于上方,即从0开始,分为i\j从两端开始往里收缩,原理和上方差不多,但速度就是要快一些.
    Runtime: 48 ms, faster than 100.00% of Python3 online submissions for Container With Most Water.
    """
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area, i, j = 0, 0, len(height) - 1
        while i < j:
            if height[i] <= height[j]:
                less = height[i]
                i += 1
            else:
                less = height[j]
                j -= 1
            new = (j - i + 1) * less
            if new > area:
                area = new
        return area