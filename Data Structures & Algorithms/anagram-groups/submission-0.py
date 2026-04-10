import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        maps: list[dict] = [collections.defaultdict(int) for _ in strs]
        for i, st in enumerate(strs):
            for c in st:
                maps[i][c] += 1
        
        tombstoned: set = set()
        full_result = []
        for i, mp_i in enumerate(maps):
            if i in tombstoned:
                continue

            this_res: set = set()
            this_res.add(i)
            for j, mp_j in enumerate(maps):
                if i == j:
                    continue
                if j in tombstoned:
                    continue
                if check_anagram(mp_i, mp_j):
                    this_res.add(j)
                    tombstoned.add(j)
            full_result.append(
                [strs[idx] for idx in this_res]
            )
            tombstoned.add(i)

        return full_result



def check_anagram(map_1: dict[chr, int], map_2: dict[chr, int]) -> bool:
    if len(map_1.keys()) != len(map_2.keys()):
        return False
    for k in map_1.keys():
        if map_1.get(k, 0) != map_2.get(k, 0):
            return False
    return True