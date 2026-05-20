class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # first positive integer missing can only be
        # from 1 to N + 1 (N+1 because there can be 0 in the nums as well)
        
        # negatives are useless
        A = nums
        for i in range(len(A)):
            if A[i] < 0:
                A[i] = 0
        # mark the values as existing or not
        for i in range(len(A)):
            val = abs(A[i])
            if val >= 1 and val <= len(A):
                # mark value as existing
                if A[val - 1] > 0:
                    A[val - 1] *= -1
                elif A[val - 1] == 0:
                    A[val - 1] = -1 * (len(A) + 1)
                
        for v in range(1, len(A) + 1):
            if A[v - 1] >= 0:
                return v
        return len(A) + 1

            



