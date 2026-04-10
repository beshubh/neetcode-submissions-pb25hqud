import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []

        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        
        res.append(nums[q[0]])
        start, end = 0, k - 1
    
        for i in range(k, len(nums)):
            start +=1
            end += 1
        
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            if q and q[0] < start:
                q.popleft()
        
            q.append(i)

            res.append(nums[q[0]])
        return res
        