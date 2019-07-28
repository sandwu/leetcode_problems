

# 题意是求天气里日期相邻但高于前一天15度

"""

# Write your MySQL query statement below

Runtime: 309 ms, faster than 95.61% of MySQL online submissions for Rising Temperature.

select t1.Id from Weather t1,Weather t2 where t1.Temperature > t2.Temperature
and TO_DAYS(t1.RecordDate)-TO_DAYS(t2.RecordDate)=1
"""