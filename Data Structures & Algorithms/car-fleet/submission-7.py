class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        data = [(s, p) for s, p in zip(speed, position)]
        data.sort(key=lambda x:x[1], reverse=True) 

        max_time = 0
        result = 0
        for s, p in data:
            time = (target - p) / s
            if time <= max_time:
                pass
            else:
                result += 1
            max_time = max(time, max_time)
        return result
            