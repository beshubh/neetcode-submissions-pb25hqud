class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max = [0] * len(height)
        suffix_max = [0] * len(height)
        prefix_max[0] = 0
        suffix_max[len(height) - 1] = len(height) - 1
        for i in range(1, len(height)):
            if height[i] > height[prefix_max[i - 1]]:
                prefix_max[i] = i
            else:
                prefix_max[i] = prefix_max[i - 1]
        
        for i in range(len(height) - 2, -1, -1):
            if height[i] > height[suffix_max[i + 1]]:
                suffix_max[i] = i
            else:
                suffix_max[i] = suffix_max[i + 1]
        water = [0] * len(height) 

        for i in range(len(height)):
            # trap
            l = height[prefix_max[i]]
            r = height[suffix_max[i]]
            print('l max: ', l, 'r max: ', r)
            if height[i] < min(l, r):
                water[i] = min(l, r) - height[i]
        print(water) 
        return sum(water)
