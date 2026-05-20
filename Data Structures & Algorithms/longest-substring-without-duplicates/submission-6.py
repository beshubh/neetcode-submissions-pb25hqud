class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = collections.defaultdict(int)
        window = set()
        max_window = 0
        i = 0
        for j in range(len(s)):
            char = s[j]
            print('window: ', window)
            while window and char in window:
                window.remove(s[i])
                i += 1
            window.add(char)
            max_window = max(max_window, len(window))
        return max_window


