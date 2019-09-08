

"""
A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs
of neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops.

一辆公共汽车有n个站，站号从0到n - 1，形成一个圆圈。我们知道所有相邻站之间的距离，其中距离[i]是站号i和(i + 1) % n之间的距离。

这辆公共汽车沿顺时针和逆时针两个方向行驶。

返回给定起点和终点之间最短的距离。
"""

class Solution(object):
    """
    解法就是分别求出顺时针和逆时针两段路，然后对应取最小即可
    """
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        left_distance = sum(distance[start:destination]) if destination>=start else sum(distance[destination:start])
        right_distance = sum(distance[destination:])+sum(distance[:start]) if destination>=start else sum(distance[:destination])+sum(distance[start:])
        return right_distance if left_distance >= right_distance else left_distance


class Solution2(object):
    """
    讨论区解法，相当于缩写了上方
    """
    def distanceBetweenBusStops(self, distance, start, destination):
        start, destination = min(start, destination), max(start, destination)
        return min(sum(distance[start:destination]), sum(distance[destination:])+sum(distance[:start]))