# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse_list(head, tail):
    prev = None
    curr = head 
    while curr:
        nxt = curr.next # save next, 4
        curr.next = prev # reverse the pointer 3 -> 2 -> 1 -> None
        prev = curr # move prev forward, 3
        if curr is tail:
            curr = nxt # move curr forward, 4
            break
        curr = nxt # move curr forward, 4
    return prev, curr


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = left = head
        count = 0
        result = None
        last_head = None
        while curr:
            count += 1
            if count % k == 0:
                rev_head, nxt  = reverse_list(left, curr)
                print('left: ', left.val, 'revhead: ', rev_head.val, 'nxt: ', nxt.val if nxt else None)
                if not result:
                    result = rev_head
                if last_head is None:
                    last_head = left
                else:
                    last_head.next = rev_head
                    last_head = left
                left.next = nxt
                left = left.next
                curr = nxt
            else:
                curr = curr.next

        return result
