


"""

Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

根据题目给的日期，推断是星期几
基姆拉尔森计算公式
W= (d+2*m+3*(m+1)/5+y+y/4-y/100+y/400+1) mod 7
在公式中d表示日期中的日数，m表示月份数，y表示年数。
注意：在公式中有个与其他公式不同的地方：
把一月和二月看成是上一年的十三月和十四月，例：如果是2004-1-10则换算成：2003-13-10来代入公式计算

"""


class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        if month == 1 or month == 2:
            month += 12
            year -=1
        iweek = (day+2*month+3*(month+1)/5+year+year/4-year/100+year/400)%7
        dict1 = {
            0:'Monday',
            1:'Tuesday',
            2:'Wednesday',
            3:'Thursday',
            4:'Friday',
            5:'Saturday',
            6:'Sunday',
        }
        return dict1[iweek]