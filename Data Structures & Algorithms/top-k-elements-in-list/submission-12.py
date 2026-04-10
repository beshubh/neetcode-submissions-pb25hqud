import collections
from sortedcontainers import SortedDict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # go through the array with a hasmap stored the count of each
        # we can even use treemap and get the top k after iterating
        # the array.
        result = []
        bucket = [None]* (len(nums) + 1)
        counts: dict = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        for n in nums:
            if bucket[counts[n]] is None:
                bucket[counts[n]] = set() 
            bucket[counts[n]].add(n)


        for v in bucket:
            if v is not None:
                result.extend(list(v))
        
        result = list(reversed(result))[:k]
        return result