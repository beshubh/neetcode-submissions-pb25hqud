class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if len(s) == 1:
        #     return s
        result = '' 
        for i in range(len(s)): # N
            for j in range(i, len(s)): # N
                substr = s[i:j + 1]
                print(substr)
                if substr == substr[::-1]:
                    if len(substr) > len(result):
                        result = substr
        return result

        
