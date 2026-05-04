class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max = [0 for _ in range(len(height))]
        suffix_max = [0 for _ in range(len(height))]
        suffix_max[-1] = len(height) - 1
        for i in range(1, len(height)):
            if height[prefix_max[i - 1]] > height[i]:
                prefix_max[i] = prefix_max[i - 1]
            else:
                prefix_max[i] = i
        
        for i in range(len(height) - 2, -1, -1):
            print('i: ', i)
            if height[suffix_max[i + 1]] > height[i]:
                suffix_max[i] = suffix_max[i + 1]
            else:
                suffix_max[i] = i
        trapped = [0 for _ in range(len(height))]
        print('heights:', height)
        print('suffix: ', suffix_max)
        print('prefix: ', prefix_max)
        for i in range(len(height)):
            trapped[i] = min(height[prefix_max[i]], height[suffix_max[i]]) - height[i]
            
        return sum(trapped)
