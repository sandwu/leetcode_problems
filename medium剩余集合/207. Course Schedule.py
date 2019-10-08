import collections


class Solution(object):
    """
    Runtime: 96 ms, faster than 29.40% of Python online submissions for Course Schedule.
    Memory Usage: 13.9 MB, less than 61.02% of Python online submissions for Course Schedule.
    """
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        forward = {i: set() for i in range(numCourses)}
        backward = collections.defaultdict(set)
        for i, j in prerequisites:
            forward[i].add(j)
            backward[j].add(i)
        stack = [node for node in range(numCourses) if not backward[node]]
        while stack:
            node = stack.pop()
            for neigh in forward[node]:
                backward[neigh].remove(node)
                if not backward[neigh]:
                    stack.append(neigh)
            backward.pop(node)
        return not backward