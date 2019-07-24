


"""
Runtime: 232 ms, faster than 96.51% of MySQL online submissions for Customers Who Never Order.

# Write your MySQL query statement below


SELECT A.Name as Customers from Customers A
WHERE A.Id NOT IN (SELECT B.CustomerId from Orders B)

"""

"""
#用外连接查询取外层为null的值
Runtime: 252 ms, faster than 79.81% of MySQL online submissions for Customers Who Never Order.

SELECT A.Name as Customers from Customers A
LEFT JOIN Orders B on  a.Id = B.CustomerId
WHERE b.CustomerId is NULL

"""