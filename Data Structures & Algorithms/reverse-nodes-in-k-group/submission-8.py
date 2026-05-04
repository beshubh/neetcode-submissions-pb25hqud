# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyHead = ListNode(-1, head)
        groupPrev = dummyHead
        while True:
            kth = self._get_kth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next
            prev = groupNext
            curr = groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            oldGroupHead = groupPrev.next
            groupPrev.next = kth # kth is reversed, so is at the head now
            groupPrev = oldGroupHead # move groupPrev forward, groupPrev stores the node just before
            # beggining of the group.
        return dummyHead.next
            
    

    def _get_kth(self, node, k):
        for _ in range(k):
            if not node.next:
                return None
            node = node.next
        return node


