"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {} # create new hashmap

        def dfs(node):

            if node in oldToNew: # if the node is already mapped, return it
                return oldToNew[node]

            copy = Node(node.val) # make copy of current node

            oldToNew[node] = copy # map old node to new node

            for n in node.neighbors: # loop through og node's neighbors
                copy.neighbors.append(dfs(n)) 
                # append dfs results to the copy's neighbor list
            
            return copy # return copy node
        
        return dfs(node) if node else None # return copy or none otherwise
        