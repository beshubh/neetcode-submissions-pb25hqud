from heapq import heappop, heappush

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        return self.val < other.val
    
    def __eq__(self, other):
        return self.val == other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for node in lists:
            if node:
                heappush(pq, (node.val, node))
        dummy = ListNode()
        if not pq:
            return None

        dummy.next = pq[0][1]
        current = dummy
        while pq:
            val, nxt = heappop(pq)
            current.next = nxt
            if nxt.next:
                heappush(pq, (nxt.next.val, nxt.next))
            current = current.next
        return dummy.next


