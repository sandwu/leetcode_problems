



class Solution:
    def __init__(self,n):
        self.result = [0] * n
        self.n = n
        self.count = 0

    def cal8queens(self,row):
        if row == self.n:
            self.printqueens()
            self.count += 1
            return
        for column in range(self.n):
            if self.isok(row,column):
                self.result[row] = column
                self.cal8queens(row+1)

    def isok(self,row,column):
        leftup = column - 1
        rightup = column + 1
        for i in range(row-1,-1,-1):
            if self.result[i] == column:return False
            if leftup >= 0:
                if self.result[i] == leftup:return False
            if rightup < self.n:
                if self.result[i] == rightup:return False
            leftup -= 1
            rightup += 1
        return True


    def printqueens(self):
        for row in range(self.n):
            for column in range(self.n):
                if self.result[row] == column:
                    print("Q ",end="")
                else:
                    print("* ",end="")
            print()
        print()

a = Solution(8)
a.cal8queens(0)
print(a.count)

class Solution4(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = [0] * n
        self.ans = []
        self.n = n
        self.count = 0
        self.cal8queens(0)
        return self.ans

    def cal8queens(self,row):
        if row == self.n:
            self.printqueens()
            self.count += 1
            return
        for column in range(self.n):
            if self.isok(row,column):
                self.result[row] = column
                self.cal8queens(row+1)

    def isok(self,row,column):
        leftup = column - 1
        rightup = column + 1
        for i in range(row-1,-1,-1):
            if self.result[i] == column:return False
            if leftup >= 0:
                if self.result[i] == leftup:return False
            if rightup < self.n:
                if self.result[i] == rightup:return False
            leftup -= 1
            rightup += 1
        return True


    def printqueens(self):
        tt = []
        for row in range(self.n):
            tmp = ""
            for column in range(self.n):
                if self.result[row] == column:
                    tmp += "Q"
                else:
                    tmp += "."
            tt.append(tmp)
        self.ans.append(tt)


a = Solution4()
print(a.solveNQueens(8))
print(a.count)