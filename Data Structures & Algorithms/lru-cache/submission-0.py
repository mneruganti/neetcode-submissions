class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None # these are the null next/prev pointers each node will have
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # empty cache hashmap

        self.left, self.right = Node(0,0), Node(0,0) # sentinel nodes for left and right pointers
        # left = LRU, # right = MRU

        # connecting the nodes to each other to make it doubly linked list
        self.left.next = self.right
        self.right.prev = self.left 

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        prev, next = self.right.prev, self.right
        node.next, node.prev = next, prev
        prev.next = next.prev = node
    

    def get(self, key: int) -> int:

        if key in self.cache:
            # remove from list
            self.remove(self.cache[key])
            # insert into list (rightmost to make it MRU)
            self.insert(self.cache[key])
            # return value
            return self.cache[key].val
        
        return -1


    def put(self, key: int, value: int) -> None:

        # if cache in key
        if key in self.cache:
            # remove from list
            self.remove(self.cache[key])
        # create new node
        self.cache[key] = Node(key, value)
        # insert into list
        self.insert(self.cache[key])
        
        # if len(list) > cap
        if len(self.cache) > self.capacity:
            # remove LRU
            lru = self.left.next # always the next node connected to the sentinel left
            self.remove(lru)
            # remove node from hashmap
            del self.cache[lru.key]
        
