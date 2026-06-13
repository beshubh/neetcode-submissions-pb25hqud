class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        cache = {}
        def backtrack(i: int, j: int):
            key = (i, j)
            if key in cache:
                return cache[key]
            if i == len(str1):
                return str2[j:]
            if j == len(str2):
                return str1[i:]
            
            if str1[i] == str2[j]:
                return str1[i] + backtrack(i + 1, j + 1)
            
            res1 = str1[i] + backtrack(i + 1, j)
            res2 = str2[j] + backtrack(i, j + 1)
            if len(res1) < len(res2):
                cache[key] = res1
                return res1
            cache[key] = res2
            return res2
        

        table = [["" for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        R, C = len(str1), len(str2)
    
        for ritr in range(R):
            table[ritr][C] = str1[ritr:]

        for citr in range(C):
            table[R][citr] = str2[citr:]

        for i in range(len(table) - 2, -1, -1):
            for j in range(len(table[0]) - 2, -1, -1):
                if str1[i] == str2[j]:
                    table[i][j] = str1[i] + table[i + 1][j + 1]
                    continue
                res1 = str1[i] + table[i + 1][j]
                res2 = str2[j] + table[i][j + 1]
                if len(res1) < len(res2):
                    table[i][j] = res1
                else:
                    table[i][j] = res2 
        return table[0][0]
