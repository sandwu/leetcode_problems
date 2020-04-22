
from functools import lru_cache

class LRUCache(object): #利用dict+list

    def __init__(self, capacity):
        self.l = []
        self.d = {}
        self.capacity = capacity

    def get(self, key):
        if self.d.has_key(key):
            value = self.d[key]
            self.l.remove(key)
            self.l.insert(0, key)
        else:
            value = None

        return value

    def set(self, key, value):
        if self.d.has_key(key):
            self.l.remove(key)
        elif len(self.d) == self.capacity:
            oldest_key = self.l.pop()
            self.d.pop(oldest_key)

        self.d[key] = value
        self.l.insert(0, key)


class LRUCache2(object): #利用Orderdict
    """
    题意是定义个LRU链表
    直接用collections的有序字典完成即可
    Runtime: 232 ms, faster than 54.38% of Python online submissions for LRU Cache.
    Memory Usage: 21.5 MB, less than 77.78% of Python online submissions for LRU Cache.
    """
    def __init__(self, capacity):
        from collections import OrderedDict
        self.array = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.array:
            value = self.array[key]
            # Remove first
            del self.array[key]
            # Add back in
            self.array[key] = value
            return value
        else:
            return -1

    def put(self, key, value):
        if key in self.array:
            # Delete existing key before refreshing it
            del self.array[key]
        elif len(self.array) >= self.capacity:
            # Delete oldest
            self.array.popitem(last=False)
        self.array[key] = value



