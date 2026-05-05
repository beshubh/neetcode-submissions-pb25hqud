class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        output = []
        used = set()
        running_perm = []
        def perm_inner():
            if len(running_perm) == len(nums):
                output.append(running_perm.copy())
                return
            for i in range(len(nums)):
                # choose
                if nums[i] not in used:
                    used.add(nums[i])
                    running_perm.append(nums[i])
                    perm_inner()
                    used.remove(nums[i])
                    running_perm.pop()
        perm_inner()
        return output
        