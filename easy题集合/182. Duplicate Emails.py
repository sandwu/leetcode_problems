


# 题意是求person表里的email重复值，用group by分组后求重复值大于1的


"""

# Write your MySQL query statement below


select Email from Person group by Email having count(*) > 1;
"""