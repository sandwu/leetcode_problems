
class Solution(object):
    """
    题意是给定一组加油站gas集合，和每到加油站所需的油cost集合，需要求得从一个点出发并回到该起点所需的油一直满足于gas集合
    解法如下，英文注释还是很清楚的
    Runtime: 40 ms, faster than 56.60% of Python online submissions for Gas Station.
    Memory Usage: 12.5 MB, less than 63.64% of Python online submissions for Gas Station.
    """
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        if (sum(gas) - sum(cost)) < 0: # if total gas at all stations is less than total cost , then no soln. exists
            return -1

        tank = 0
        src  = 0 # starting from index 0
        cur  = 0
        while True:
            tank += gas[cur]         # car is at 'cur', fill the tank
            if tank - cost[cur] < 0: # car can't move to next stop, let car begin from next stop
                tank = 0             # empty the tank
                src  = (cur +1 ) %n     # update src
                cur  = src           # move to src
                continue             # move back to start of the loop
            tank -= cost[cur]        # moving to next emptied the gas by cost[cur]
            cur   = (cur +1) % n  # reached next
            if src == cur:  # did complete cycle?
                return src  # return start