# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# solution below
from typing import Optional


class ListNode:
    def __init__(self, val=0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head: ListNode, tail: ListNode) -> ListNode:
        cur, prev = head, None
        while cur:
            cur_next = cur.next
            cur.next = prev
            prev = cur
            if cur == tail:
                break
            cur = cur_next

        cur = prev 
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        cur, left, count = head, head, 0
        return_head = None
        tail = None
        while cur:
            count += 1
            if count % k == 0:
                cur_next = cur.next
                reverse_head = self.reverse(left, cur)
                if tail:
                    tail.next = reverse_head
                tail = left
                left.next = cur_next 
                left = cur_next
                cur = cur_next
                if return_head is None:
                    return_head = reverse_head
            else:
                cur = cur.next
        return return_head
