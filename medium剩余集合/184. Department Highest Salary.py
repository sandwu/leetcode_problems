


#题意是求给定table最高的salary，并且是连接查询

"""

# Write your MySQL query statement below

select d.name as department, e.name as employee, e.salary as salary

from employee as e

join department as d on e.departmentid = d.id

where (d.id, e.salary) in

(select department.id, max(salary)
 from employee
 join department on department.id = employee.departmentid
group by departmentid)

"""