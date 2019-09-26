


#题目给定两列，求指定一列连续的三个相同





"""
# Write your MySQL query statement below

select distinct l1.Num as ConsecutiveNums from Logs l1
left join Logs l2 on l1.Id=l2.Id-1
left join Logs l3 on l1.Id=l3.Id+1
where l1.Num=l2.Num and l1.Num=l3.Num

"""