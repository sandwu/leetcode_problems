
class Solution(object):
    """
    参考讨论区：https://leetcode.com/problems/invalid-transactions/discuss/366332/python-sort-solution
    题意是一个较为复杂的场景题，给定列表，列表里包含1各个字符串，每个字符串包含人名、时间、金额、城市4个属性，每个属性
    用逗号隔开，要求求出不满足这两个特征的字符串：1.金额高于1000  2.人名相同，但城市不同，而两者之间时间间隔小于60的

    解法：该解法最重要的在于一开始进行排序，排序规则为人名+时间，所以除了边界相邻的都是相同名字，接着定义一个flag用于
    判断是否满足第2个特征，考虑到能满足第2个特征的可能多个，所以if duplicate后还要继续while遍历，接着判断是否满足第1
    个特征，因为结果集是set，所以无需担心重复值
    """
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        t = [x.split(',') for x in transactions]
        t.sort(key = lambda x: (x[0] ,int(x[1])))
        i = 0
        ret = set()
        while i < len(t):
            j = i + 1
            duplicate = False
            while j < len(t) and t[j][0] == t[i][0] and int(t[j][1]) - int(t[i][1]) <= 60:
                if t[j][3] != t[i][3]:
                    duplicate = True
                j += 1

            if duplicate:
                k = i
                while k < j:
                    ret.add(','.join(t[k]))
                    k += 1
            elif int(t[i][2]) > 1000:
                ret.add(','.join(t[i]))
            i += 1
        return ret