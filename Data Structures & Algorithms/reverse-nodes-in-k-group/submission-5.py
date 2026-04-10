# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



def reverse_list(head, tail):
    curr = head
    prev = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        if curr is tail:
            curr = nxt
            break 
        curr = nxt
    return prev, curr

class Solution:
    def get_kth(self, node, k):
        curr = node
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = group_prev = head
        last_group_prev = None 
        count = 0
        result = None
        while curr:
            count += 1
            if count % k == 0:
                t, nxt = reverse_list(group_prev, curr)
                if not result:
                    result = t
                if last_group_prev is not None:
                   last_group_prev.next = t 
                last_group_prev = group_prev
                group_prev.next = nxt
                group_prev = group_prev.next
                curr = nxt
            else: 
                curr = curr.next
        return result
