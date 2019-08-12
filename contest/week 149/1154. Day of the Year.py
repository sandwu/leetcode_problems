



class Solution:
    """
    题意是求给定格式"2019-01-04"，求对应的当年的天数
    """
    def dayOfYear(self, date: str) -> int:
        list1 = [0,
                 31,
                 28,
                 31,
                 30,
                 31,
                 30,
                 31,
                 31,
                 30,
                 31,
                 30]

        year ,month ,day = date.split("-")
        if self.isleapyear(int(year)):
            list1[2] = 29
        for i in range(1 ,len(list1)):
            list1[i] = list1[ i -1 ] +list1[i]
        return list1[int(month ) -1] + int(day)


    def isleapyear(self ,year):
        if year % 4 ==0:
            if year % 100 == 0:
                if year % 400 ==0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False