class Solution:

    def bin_search(self, a: list[int], l: int, r: int, target: int):
        while l <= r:
            mid = (l + r) // 2
            if a[mid] == target:
                return mid
            if target < a[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1

    def search(self, nums: List[int], target: int) -> int: 
        # 5 1 3 target = 3
        # 0 1 2
        left, right = 0, len(nums) - 1 # 0, 2
        while left <= right: # 0 <= 2
            if nums[left] < nums[right]: # array is sorted
                return self.bin_search(nums, left, right, target)
            mid = (left + right) // 2 # 1
            pivot = nums[mid] # 1
            if pivot == target:
                return mid
        
            # we are currently in the left sub array
            if nums[left] <= pivot:
                if target > pivot or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1 
            # we are in the right sorted subarray
            else:
                if target < pivot or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

