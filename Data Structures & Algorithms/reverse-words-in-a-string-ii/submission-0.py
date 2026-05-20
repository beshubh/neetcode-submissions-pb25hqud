class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i <= j:
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1
        
        i, j = 0, 0
        while j < len(s):
            c = s[j]
            if c.isspace():
                l, r = i, j - 1
                while l <= r:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1

                i = j + 1
                j = j + 1
            else:
                j += 1
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        
        
