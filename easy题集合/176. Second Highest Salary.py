

#题意是用sql求表里第二大的值

"""
我的解法：Runtime: 143 ms, faster than 56.23% of MySQL online submissions for Second Highest Salary.
# Write your MySQL query statement below
select max(Salary) as SecondHighestSalary from Employee where Salary not in (select max(Salary) from Employee)
"""


"""
# 讨论区的解法：Runtime: 130 ms, faster than 84.36% of MySQL online submissions for Second Highest Salary.
# Write your MySQL query statement below
select (
  select distinct Salary from Employee order by Salary Desc limit 1 offset 1
)as SecondHighestSalary
"""