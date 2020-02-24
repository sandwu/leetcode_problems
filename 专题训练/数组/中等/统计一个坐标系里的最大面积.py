
"""
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""



class Solution:
    def maxArea(self,height):
        now_maxarea = start = 0
        end = len(height) - 1
        while start < end:
            now_maxarea = max(now_maxarea, (end - start) * min(height[start], height[end]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return now_maxarea