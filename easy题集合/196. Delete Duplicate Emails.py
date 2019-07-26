

#题意是求满足数据表里不重复的email所在行的所有行


"""
Runtime: 781 ms, faster than 35.94% of MySQL online submissions for Delete Duplicate Emails.
利用自身来两表连接，并删除左边和右边重复的值，思路很巧妙

# Write your MySQL query statement below

DELETE p1
FROM Person p1, Person p2
WHERE p1.Email = p2.Email AND
p1.Id > p2.Id

"""