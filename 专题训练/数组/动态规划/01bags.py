




"""
cw表示当前已经装进去的物品的重量和；i表示考察到哪个物品了；
w背包重量；items表示每个物品的重量；n表示物品个数
假设背包可承受重量100，物品个数10，物品重量存储在数组a中，那可以这样调用函数：
"""
class Solution:
    def ff(self):
        self.max_value = float('-inf')
        self.dfs(0,0,0,10,100)


    def dfs(self,i,cw,items,n,w):

        if cw == w or i == n:
            if cw > self.max_value:
                max_value = cw
                return
        self.dfs(i+1,cw,items,n,w)
        if (cw+items[i]) <= cw:
            self.dfs(i+1,cw+items[i],items,n,w)


"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
 
"""


class Solution4(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        s = sum(nums)
        if s % 2: return False
        s = s / 2
        self.dict1 = {}
        return self.dfs(nums, 0, s)

    def dfs(self, nums, start, target):
        if (start, target) in self.dict1:
            return self.dict1[(start, target)]
        if target < 0:
            return
        elif target == 0:
            return True
        for i in range(start, len(nums)):
            if self.dfs(nums, i + 1, target - nums[i]):
                return True
        self.dict1[(start, target)] = False
        return False

"""
322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1

"""

class Solution3(object): #超时
    def coinChange(self, coins, amount):
        self.min_nums = float('inf')
        self.dfs(0,coins,amount,1)
        return self.min_nums if self.min_nums != float('inf') else -1


    def dfs(self,index,coins,amout,count):
        if amout < 0:return 0
        if amout-coins[index] == 0:
            self.min_nums=min(self.min_nums,count)
            return
        for i in range(index,len(coins)):
            self.dfs(i,coins,amout-coins[i],count+1)



"""
In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:

The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.
 

Example 1:

Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
 

Example 2:

Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

"""

class Solution6(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        self.max_value = float('-inf')
        self.dfs(0,strs,m,n,0)
        return self.max_value

    def dfs(self,index,strs,m,n,count):
        if m<0 or n<0:return 0
        for i in range(index,len(strs)):
            count0,count1 = self.count_str_01(strs[i])
            if m>=0 and n >=0:
                if m==n==0:return
                self.max_value = max(self.max_value,count)
            self.dfs(index+1,strs,m-count0,n-count1,count+1)


    def count_str_01(self,str):
        count0 = 0
        count1 = 0
        for i in str:
            if i=="0":count0+=1
            else:count1+=1
        return count0,count1



