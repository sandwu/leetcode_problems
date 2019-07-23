

#题意竟然是求两表连接。。。

# Write your MySQL query statement below
"""
select t1.FirstName,t1.LastName,t2.City,t2.State from Person t1 left join Address t2 on t1.PersonId=t2.PersonId;
"""