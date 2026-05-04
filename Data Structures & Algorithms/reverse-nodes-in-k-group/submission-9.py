# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1, head)
        group_prev = dummy_head
        while True:
            kth = self._get_kth(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            # reverse the group
            prev = group_next # prev is the group next, so we can connect the head to right node
            curr = group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            old_group_head = group_prev.next # firs time, dummy -> 1 (group_prev.next) -> 2 -> 3
            # after reverse, k = 2
            # 2 -> 1 <- dummy
            #   group_prev ^
            group_prev.next = kth # dummy -> 2 -> 1, as kth is reversed.
            group_prev = old_group_head # dummy -> 2 -> 1(group_prev), as 1 is the previous of 3 which is the start of new group
        
        return dummy_head.next
    
    def _get_kth(self, node, k):
        for _ in range(k):
            node = node.next
            if not node:
                return None
        return node
            

            
