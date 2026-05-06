# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # dummy -> 1 -> 2 -> 3 | 4 -> 5 -> 6 | 7 -> 8
        # dummy -> 3 -> 2 -> 1* -> 4 -> 5 -> 6 | 7 -> 8
        dummy_head = ListNode(-1, head)
        group_prev = dummy_head
        while True:
            kth: ListNode | None = self._get_kth(group_prev, k) # 3
            if not kth:
                break
            print('group prev: ', group_prev.val)
            group_next = kth.next # 4
            # reverse
            prev = group_next # 3
            curr = group_prev.next # 4
            #  3 -> 2 -> 1 <- dummy
            #            |.
            #            4
            while curr != group_next: # 4 != 4, False
                tmp = curr.next # 4
                curr.next = prev # 2
                prev = curr 
                curr = tmp
            
            # prev = 3, curr = 4
            old_group_head = group_prev.next # 1
            # connect 
            # current 3 -> 2 -> 1* <- ^dummy | * denotes old group head, ^ denotes group prev
            group_prev.next = kth
            # after above dummy -> 3 -> 2 -> 1
            # update group prev 
            group_prev = old_group_head # as 1 is the new group_prev for next iteration
            print('***')
    
        return dummy_head.next
    
    def _get_kth(self, node, k: int):
        for _ in range(k):
            node = node.next
            if node is None:
                return None
        return node


