class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [3, 4, 5, 1, 2]
        """
        l, r = 0, len(nums) - 1
        ans = float('inf')
        count = 0
        while l <= r:
            count += 1
            mid = (l + r) // 2
            pivot = nums[mid]
            # in the sorted array mid should not be greater than right most
            if pivot > nums[r]:
                # if it is then then the smaller segment exists on the right.
                l = mid + 1
            else:
                # if it is not then mid could be the potential answer
                # it's potential not the answer, as we could be far right 
                # so we try to move to the left to cover more potential answers
                ans = min(ans, pivot)
                r = mid - 1
        return ans
            
