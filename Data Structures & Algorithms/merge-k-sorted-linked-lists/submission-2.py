# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not lists[0]:
            return None

        head = ListNode(0)
        current = head
        while True:
            min_node, midx = None, -1
            if all(node is None for node in lists):
                break
            for i, node in enumerate(lists):
                if node is None:
                    continue
                if min_node is None or node.val < min_node.val:
                    min_node, midx = node, i
            if min_node is None:
                break
            current.next = min_node
            current = current.next
            lists[midx] = lists[midx].next
        return head.next
