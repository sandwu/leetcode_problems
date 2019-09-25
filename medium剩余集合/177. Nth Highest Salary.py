





"""
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M=N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT e1.Salary FROM Employee e1
      WHERE M = (SELECT COUNT(DISTINCT e2.Salary) FROM Employee e2 where e2.Salary>e1.Salary)
  );
END

"""