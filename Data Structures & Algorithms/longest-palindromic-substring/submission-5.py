class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_idx = -1
        res_len = -1 
        for i in range(len(s)):
            # odd case
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > res_len:
                    res_len = right - left + 1
                    res_idx = left
                left -= 1
                right += 1
            
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > res_len:
                    res_idx = left
                    res_len = right - left + 1
                left -= 1
                right += 1
            
        print(res_idx, res_len)
        return s[res_idx:res_idx + res_len]
