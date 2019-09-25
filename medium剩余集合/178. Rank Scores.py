



"""
Runtime: 193 ms, faster than 91.22% of MySQL online submissions for Rank Scores.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rank Scores

# Write your MySQL query statement below
SELECT Score, CONVERT((@rank := CASE
    WHEN @rankval = Score THEN @rank
    WHEN (@rankval := Score) IS NOT NULL THEN @rank + 1
END), UNSIGNED INTEGER) AS Rank
FROM Scores, (SELECT @rank := 0, @rankval := NULL) AS x
ORDER BY Score DESC

"""