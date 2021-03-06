import heapq


class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.a = []
        self.limit = capacity
        self.q = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        i = self._get()
        if i != -1:
            self.a[i].append(val)
        else:
            if not self.a or len(self.a[-1]) == self.limit:
                self.a.append([])
            self.a[-1].append(val)

    def pop(self):
        """
        :rtype: int
        """
        while self.a:
            if self.a[-1]:
                v = self.a[-1].pop()
                while self.a and not self.a[-1]:
                    self.a.pop()
                return v
            self.a.pop()
        return -1

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index >= len(self.a) or not self.a[index]:
            return -1
        v = self.a[index].pop()
        heapq.heappush(self.q, index)
        return v

    def _get(self):
        while self.q:
            i = heapq.heappop(self.q)
            if i < len(self.a) and len(self.a[i]) < self.limit:
                return i
        return -1



# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)