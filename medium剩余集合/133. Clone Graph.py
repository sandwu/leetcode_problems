


"""
# Definition for a Node.

"""

class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        self.node_dict = {}
        def clone(node):
            if not node: return
            if node not in self.node_dict:
                self.node_dict[node] = Node(node.val,[])
                for nei in node.neighbors:
                    clone(nei)
            return
        clone(node)
        for key in self.node_dict:
            self.node_dict[key].neighbors = [self.node_dict[nei] for nei in key.neighbors]
        return self.node_dict[node]