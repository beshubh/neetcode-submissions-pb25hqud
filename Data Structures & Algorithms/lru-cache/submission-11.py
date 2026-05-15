from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    key: Any
    value: Any
    next: Optional['Node']  = None
    prev: Optional['Node'] = None

"""We will keep the recent at the tail"""
class LList:
    def __init__(self) -> None:
        self._head = Node('-head', '-head')
        self._tail = Node('-tail', '-tail')
        self._head.next, self._tail.prev = self._tail, self._head
    
    def add(self, node: Node):
        """Add to the tail"""
        # new node 3
        # head <-> tail
        curr_tail_prev = self._tail.prev # head
        self._tail.prev = node # 3 <- tail
        curr_tail_prev.next = node # type: ignore # head -> 3 <- tail
        node.prev = curr_tail_prev # head <-> 3 <- tail
        node.next = self._tail # head <-> 3 <-> tail

    def remove(self, node: Node):
        """ Remove node from list""" 
        # node: 1
        # list: head <-> 1 <-> 2 <-> 3 <-> tail
        node_prev = node.prev # head
        node_next = node.next # 2
        node_prev.next = node_next # head -> 2
        node_next.prev = node_prev # head <-> 2
        # list: head <-> 2 <-> 3 <-> tail
    
    def pop_head(self):
        # head <-> 1 <-> 2 <-> 3 <-> tail
        actual_head = self._head.next
        print('actual head: ', actual_head)
        if actual_head is self._tail:
            raise ValueError('list is emtpy')
        self.remove(actual_head) # type: ignore
        return actual_head
    

class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._size = 0
        self._list = LList()
        self._datastore: dict[int, Node] = {}

    def get(self, key: int) -> int:
        node = self._datastore.get(key)
        if not node:
            return -1
        self._list.remove(node)
        self._list.add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self._datastore.get(key)
        if node:
            node.value = value
            self._list.remove(node)
            self._list.add(node)
        else:
            node = Node(key=key, value=value)
            self._list.add(node)
            self._datastore[key] = node
            self._size += 1
        
        if self._size > self._capacity:
            node = self._list.pop_head()
            self._datastore.pop(node.key, None)
            self._size -= 1



        
