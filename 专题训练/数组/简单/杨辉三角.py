

class PascalTriangle:
    def pascaltriangle(self,numRows):
        res = []
        for i in range(len(numRows)):
            tmp = []
            tmp.append(1)

            if i > 1:
                for j in range(i-1):
                    num = res[i-1][j] + res[i-1][j+1]
                    tmp.append(num)
            if i != 0:
                tmp.append(1)
            res.append(tmp)
        return res

#杨辉三角2，根据给定的数字n求得第n行的数组排列
#直接照搬1的解法

class PascalTriangle2:
    def pascaltriangle2(self,rowIndex):
        res = []
        for i in range(rowIndex+1):
            tmp = []
            tmp.append(1)
            if i > 1:
                for j in range(i-1):
                    num = res[i-1][j] + res[i-1][j+1]
                    tmp.append(num)
            if i != 0:
                tmp.append(1)
            res.append(tmp)
        return res[-1]