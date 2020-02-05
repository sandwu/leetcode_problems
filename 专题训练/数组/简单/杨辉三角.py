

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