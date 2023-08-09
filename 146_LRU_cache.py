class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left      

    def remove(self, node): # remove FROM LRU_Cache
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev         
    
    def insert(self, node): # insert INTO LRU_Cache (rightmost)
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.prev, node.next = prev, nxt
        
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key]) # brings it to rightmost as most recent
            return self.cache[key].val 
        else: 
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key]) 

        if len(self.cache) > self.capacity:
            # grab the least recently used Node 
            # remove it from the LRU_Cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
param_1 = obj.get(key)
obj.put(key,value)

