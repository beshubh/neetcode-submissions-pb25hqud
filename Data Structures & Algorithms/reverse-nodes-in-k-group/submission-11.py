# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        group_prev = dummy_head
        while True:
            kth = self._get_kth(group_prev, k)

            if not kth:
                break
            group_next = kth.next
            # reverse 
            prev = group_next
            curr = group_prev.next
            while curr != group_next:
                tmp = curr.next 
                curr.next = prev 
                prev = curr
                curr = tmp
            
            # connection 
            old_gh = group_prev.next
            group_prev.next = kth
            group_prev = old_gh
            
        return dummy_head.next
    
    def _get_kth(self, node, k: int):
        for _ in range(k):
            node = node.next
            if node is None:
                return None
        return node