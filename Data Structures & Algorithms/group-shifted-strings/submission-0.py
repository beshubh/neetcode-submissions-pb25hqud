import collections


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        patterns = collections.defaultdict(list)
        for string in strings:
            pattern = []
            for i in range(1, len(string)):
                diff = (ord(string[i]) - ord(string[i - 1])) % 26
                pattern.append(diff)
            patterns[tuple(pattern)].append(string)
        print(patterns)
        result = []
        for k, v in patterns.items():
            result.append(v)

        return result



