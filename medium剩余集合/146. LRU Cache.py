
class LRUCache(object):
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
            k, v = self.array.iteritems().next()
            del self.array[k]
        self.array[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)