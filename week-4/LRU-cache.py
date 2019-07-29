class LRUCache:
    class Node():
        def __init__(self, key=0, val=0):
            self.key = key
            self.val = val
            self.before = None
            self.after = None

    def __init__(self, capacity: int):
        self.lookup = {}
        self.head = self.Node()
        self.tail = self.Node()
        self.head.after = self.tail
        self.tail.before = self.head
        self.capacity = capacity
        self.current_amount = 0

    def get(self, key: int) -> int:
        if self.lookup.get(key):
            self.move_top(self.lookup[key])
            return self.lookup[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.lookup.get(key):
            self.lookup[key].val = value
            self.move_top(self.lookup[key])
        else: # value was not found
            # Save previous most freq node
            temp = self.head.after
            
            # Create new node and make connections from head and prev freq node
            self.head.after = self.Node(key, value)
            self.head.after.before = self.head
            self.head.after.after = temp
            temp.before = self.head.after
            
            # increase current amount
            self.current_amount += 1
            
            # insert into lookup table
            self.lookup[key] = self.head.after
            
            # if over capacity, delete least freq
            if self.current_amount > self.capacity:
                self.remove(self.tail.before)
    
    def move_top(self, node):
        node = self.remove(node)
        self.put(node.key, node.val)
        
    def remove(self, node):
        # remove from lookup
        self.lookup.pop(node.key)
        
        # remove from location
        temp_before = node.before
        temp_after = node.after
        temp_before.after = temp_after
        temp_after.before = temp_before
        
        self.current_amount -= 1
        
        return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)