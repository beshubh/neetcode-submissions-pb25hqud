from collections import defaultdict


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [10, 8, 5, 3, 0]
        # [2, 4, 1, 3, 1]

        data = [(s, p) for s, p in zip(speed, position)]
        print(data)
        data = reversed(sorted(data, key= lambda x: x[1]))  # [(1, 7), (2, 4), (2, 1), (1, 0)]
        maxTime = 0 # 4.5
        res = 0 # 3
        for s, p in data: # (s = 1, p = 0)
            t = (target - p) / s # t = 10 - 0/ 1= 10
            if not t <= maxTime: #  not 10 <= 4.5, yes
                res += 1
            maxTime = max(maxTime, t) 
        return res




        