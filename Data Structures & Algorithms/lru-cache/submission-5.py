
from typing import Any
from dataclasses import dataclass, field


@dataclass
class Node:
    key: Any
    value: Any
    next: Node | None = None
    prev: Node | None = None


@dataclass
class DLinkedList:
    _head: Node = field(default_factory=lambda: Node('dh', 'dh'))
    _tail: Node = field(default_factory=lambda: Node('dt', 'dt'))

    def __post_init__(self) -> None:
        self._head.next, self._tail.prev = self._tail, self._head

    def add(self, node: Node):
        # add to the tail
        # get current tail
        cur_tail_prev = self._tail.prev
        # set tail prev to the node
        self._tail.prev = node
        # set cur_tail_prev's next to the node
        cur_tail_prev.next = node

        # set node's next to the tail
        node.next = self._tail
        node.prev = cur_tail_prev

    def remove(self, node: Node):
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node_next
        node_next.prev = node_prev

    def remove_head(self):
        head_next = self._head.next
        self._head.next = self._head.next.next
        head_next.next.prev = self._head
        return head_next


class LRUCache:
    def __init__(self, capacity: int):
        self._list = DLinkedList()
        self._store = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        node = self._store.get(key)
        if not node:
            return -1
        # remove the node and add to the tail
        self._list.remove(node)
        self._list.add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self._store:
            node = self._store[key]
            node.value = value
            self._list.remove(node)
            self._list.add(node)
        else:
            node = Node(key=key, value=value)
            self._store[key] = node
            self._list.add(node)

        while len(self._store) > self.capacity:
            node = self._list.remove_head()
            del self._store[node.key]
