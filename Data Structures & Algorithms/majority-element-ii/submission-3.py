class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        candidate1 = None
        candidate2 = None
        count1 = 0
        count2 = 0

        for x in nums:
            if x == candidate1:
                count1 += 1
            elif x == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = x
                count1 = 1
            elif count2 == 0:
                candidate2 = x
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        n = len(nums)
        result = []
        if nums.count(candidate1) > n / 3:
            result.append(candidate1)
        if candidate2 != candidate1 and nums.count(candidate2) > n/3:
            result.append(candidate2)
        return result