


#本质是自下而上、状态转移方程、



"""
cw表示当前已经装进去的物品的重量和；i表示考察到哪个物品了；
w背包重量；items表示每个物品的重量；n表示物品个数
假设背包可承受重量10，物品个数5，物品重量存储在数组a中，那可以这样调用函数：
"""
class Solution:
    def ff(self):
        self.max_value = float('-inf')
        items = [2,2,4,6,3]
        n = len(items)
        w = 16
        self.dfs(0,0,items,n,w)
        return self.max_value


    def dfs(self,index,cw,items,n,w):
        if cw > w:return
        if cw == w or index == n:
            self.max_value = max(self.max_value,cw)
            return
        for i in range(index,n):
            self.dfs(i+1,cw+items[i],items,n,w)

a = Solution()
print(a.ff())