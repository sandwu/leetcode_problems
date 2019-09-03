


"""
Example 1:

Input: calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3
Output: 0
Explaination: calories[0], calories[1] < lower and calories[3], calories[4] > upper, total points = 0.
Example 2:

Input: calories = [3,2], k = 2, lower = 0, upper = 1
Output: 1
Explaination: calories[0] + calories[1] > upper, total points = 1.
Example 3:

Input: calories = [6,5,0,0], k = 2, lower = 1, upper = 5
Output: 0
Explaination: calories[0] + calories[1] > upper, calories[2] + calories[3] < lower, total points = 0.
"""



class Solution(object):
    #题意比较难理解，这里的k是指连续k天的卡路里，很难理解这个连续k天是什么意思，讨论区通过滑动窗口来实现
    #即连续k天相当于有k个数字的滑动窗口，比如第三个例子，滑动窗口分别为：[6,5],[5,0],[0,0]，
    #然后计算每个滑动窗口里的和为正还是负，正则+1，负则-1
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sm = sum(calories[:k])
        points = (sm>upper) - (sm<lower)
        for i in range(k,len(calories)):
            sm += calories[i] - calories[i-k]
            points += (sm>upper) - (sm<lower)
        return points