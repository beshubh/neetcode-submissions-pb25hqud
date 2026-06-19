# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        indeg = {c: 0 for c in range(n)}
        outdeg = {c: 0 for c in range(n)}

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if knows(i, j):
                    indeg[j] += 1
                    outdeg[i] += 1
        celeb = -1
        maxk = 0

        for i in range(n):
            if outdeg[i] == 0 and indeg[i] > maxk:
                maxk = indeg[i]
                celeb = i
        
        return celeb if maxk == n - 1 else -1