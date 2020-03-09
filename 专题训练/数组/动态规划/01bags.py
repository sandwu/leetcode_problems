




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
        self.dfs(i+1,cw+items[i],items,n,w)
