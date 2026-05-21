class Node:

    def __init__(self, key, value, next = None, prev = None, usecount = 0) -> None:
        self.key = key
        self.value = value
        self.usecount = usecount
        self.next = next
        self.prev = prev

class DList:

    def __init__(self) -> None:
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self._size = 0
        self.head.next, self.tail.prev = self.tail, self.head
    
    def remove(self, node):
        assert node is not None
        assert node is not self.head
        assert node is not self.tail

        node_prev = node.prev
        node_next = node.next
        assert node_prev is not None
        assert node_next is not None

        node_prev.next = node_next
        node_next.prev = node_prev
        self._size -= 1
    
    def add(self, node):
        tail_prev = self.tail.prev 
        tail_prev.next = node
        node.prev = tail_prev
        node.next = self.tail
        self.tail.prev = node
        self._size += 1
    
    def pop_left(self) -> Node:
        head_next = self.head.next
        if head_next is self.tail:
            raise ValueError('list is empty')
        self.remove(head_next)
        return head_next

    @property 
    def size(self):
        return self._size


class LFUCache:

    def __init__(self, capacity: int):
        self._store = {}
        self._capacity = capacity
        self._size = 0
        self._freq_map: dict[int, DList] = collections.defaultdict(DList)
        self._least_freq = 1


    def get(self, key: int) -> int:
        node = self._store.get(key)
        if node is None:
            return -1
        # every time a node is used, its usecount should increase
        # we should maintain lru least for lfu fallback
        self._update_freq(node)
        return node.value
    
    def _update_freq(self, node: Node):
        self._freq_map[node.usecount].remove(node)
        if node.usecount == self._least_freq and self._freq_map[self._least_freq].size == 0:
            self._least_freq += 1
        # use setter 
        node.usecount += 1
        self._freq_map[node.usecount].add(node)


    def put(self, key: int, value: int) -> None:
        # if we are out of capacity, we should remove the least frequent key
        if self._size  + 1 > self._capacity:
            node = self._freq_map[self._least_freq].pop_left()
            del self._store[node.key]

            if self._freq_map[self._least_freq].size == 0:
                self._least_freq += 1
            self._size -= 1
    
        node = self._store.get(key)
        if node:
            node.value = value
            self._update_freq(node)
        else:
            node = Node(key=key, value=value, usecount=1)
            self._store[key] = node
            self._size += 1

            # reset least freq 
            self._least_freq = 1
            self._freq_map[node.usecount].add(node) 


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)