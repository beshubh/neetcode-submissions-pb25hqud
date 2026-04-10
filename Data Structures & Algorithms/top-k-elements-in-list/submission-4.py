import collections
from sortedcontainers import SortedDict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # go through the array with a hasmap stored the count of each
        # we can even use treemap and get the top k after iterating
        # the array.
        counts: dict = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        result = []
        for _ in range(k):
            top_count = -1
            top_num = None
            for k, v in counts.items():
                if top_count < v:
                    top_count = v
                    top_num = k
            result.append(top_num)
            del counts[top_num] 
        return result