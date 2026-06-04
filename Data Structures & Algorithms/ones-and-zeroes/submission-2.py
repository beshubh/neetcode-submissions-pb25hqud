class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = []
        for s in strs:
            counts.append(collections.Counter(s))
        memo = {} 
        def find_max(i: int, ones, zeroes):
            if ones == 0 and zeroes == 0:
                return 0
            
            if i == len(strs):
                return 0
            key = (i, ones, zeroes)
            if key in memo:
                return memo[key]
            i_zeros = counts[i].get('0', 0)
            i_ones = counts[i].get('1', 0)
            result = 0
            if i_ones <= ones and i_zeros <= zeroes:
                result = max(result, 1 + find_max(i + 1, ones - i_ones, zeroes - i_zeros))
            # exclude ith
            result = max(result, find_max(i + 1, ones, zeroes))
            memo[key] = result
            return result
        result = find_max(0, n, m)
        return result

