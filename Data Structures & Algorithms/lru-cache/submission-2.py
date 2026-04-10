from typing import Any
from dataclasses import dataclass


@dataclass
class Node:
    def __init__(self, key: Any, value: Any, prev: Node | None = None, next: Node | None = None):
        self.value = value
        self.key = key
        self.prev = prev
        self.next = next
    
    def __str__(self):
        return f'<Node: k:{self.key}, v: {self.value}>'


class DLinkedList:
    def __init__(self, capacity: int):
        node = Node('dummy', 'dummyval')
        self._head = node
        self._tail = node
        self._capacity = capacity
        self._size = 0

    def _remove_from_list(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        if prev_node:
            if next_node:
                prev_node.next = next_node
                next_node.prev = prev_node
            else:
                # node is the tail node
                self._tail = prev_node
                prev_node.next = None
        else:
            # do nothing, already at the top
            pass
        self._size -= 1

    def move_to_head(self, node: Node):
        self._remove_from_list(node)
        self.add_to_head(node)

    def pop_tail(self) -> Node | None:
        self._size -= 1

        tail_prev = self._tail.prev
        tail = self._tail

        if tail_prev is None:
            self._head.next = None
            self._tail = self._head
            return tail
        tail_prev.next = None
        self._tail = tail_prev
        return tail

    def add_to_head(self, node: Node):
        self._size += 1
        head_next = self._head.next
        if head_next is None:
            self._head.next = node
            node.prev = self._head
            self._tail = node
        else:
            node.next = head_next
            node.prev = self._head
            head_next.prev = node
            self._head.next = node

    def size(self):
        return self._size


class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._list = DLinkedList(capacity)
        self._cache = {}

    def get(self, key: int) -> int:
        node: Node | None = self._cache.get(key, None)
        if node is None:
            return -1
        self._list.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            node: Node = self._cache[key]
            node.value = value
            self._list.move_to_head(node)
        else:
            node = Node(key=key, value=value)
            self._list.add_to_head(node)
            self._cache[key] = node
        while self._list.size() > self._capacity:
            # remove one from tail
            node: Node | None = self._list.pop_tail()
            print('node to remove', node)
            if node and node.key in self._cache:
                del self._cache[node.key]
