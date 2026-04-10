import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # m = len(strs), n = len of longest str in strs

        # step build, time = O(m * n), space = O(m), as each map itself will just be a constant space (chars are constant)
        counts: list[list[int]] = [[0] * 26 for _ in strs]
        for i, st in enumerate(strs):
            for c in st:
                counts[i][ord(c) - 97] += 1

        storeage = collections.defaultdict(list)
        for i, count in enumerate(counts):
            count = tuple(count)
            storeage[count].append(i)
        res = []
        for k, v in storeage.items():
            res.append(
                [strs[i] for i in v]
            )
        return res


def check_anagram(map_1: dict[chr, int], map_2: dict[chr, int]) -> bool:
    if len(map_1.keys()) != len(map_2.keys()):
        return False
    for k in map_1.keys():
        if map_1.get(k, 0) != map_2.get(k, 0):
            return False
    return True