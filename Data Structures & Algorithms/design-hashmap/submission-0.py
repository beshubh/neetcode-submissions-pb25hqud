from typing import Optional


class ListNode:

    def __init__(
        self,
        key: int, 
        value: int,
        prev: Optional['ListNode'] = None,
        next: Optional['ListNode'] = None
    ) -> None:
        self._key = key
        self._value = value
        self.next = next
        self.prev = prev

    @property
    def key(self):
        return self._key
    
    @property
    def value(self):
        return self._value


class DList:

    def __init__(self) -> None:
        self._head = ListNode(-1, -1)
        self._tail = ListNode(-1, -1)
        self._head.next, self._tail.prev = self._tail, self._head
    
    def remove(self, node: ListNode):
        assert node is not None
        node_prev = node.prev
        node_next = node.next

        assert node_prev is not None
        assert node_next is not None
        node_prev.next = node_next
        node_next.prev = node_prev
    
    def add(self, node: ListNode):
        assert node is not None
        tail_prev = self._tail.prev

        assert tail_prev is not None
        tail_prev.next = node
        node.next = self._tail
        node.prev = tail_prev
        self._tail.prev = node
    
    def find(self, key: int):
        cur = self._head.next
        while cur != None:
            if cur._key == key:
                return cur
            cur = cur.next
        return None

class MyHashMap:

    def __init__(self):
        self._capacity = 1001
        self._store = [DList()]*self._capacity

    def _hash(self, key: int):
        return key % self._capacity

    def put(self, key: int, value: int) -> None:
        hkey = self._hash(key)
        dlist = self._store[hkey]
        node = dlist.find(key)
        if node:
            node._value = value
        else:
            node = ListNode(key=key, value=value)
            self._store[hkey].add(node)

    def get(self, key: int) -> int:
        hkey = self._hash(key)
        node = self._store[hkey].find(key)
        if node is None:
            return -1
        return node.value

    def remove(self, key: int) -> None:
        hkey = self._hash(key)
        dlist = self._store[hkey] 
        node = dlist.find(key)
        if node is None:
            return None
        dlist.remove(node)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)