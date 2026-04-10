class Solution:
    def findMedianSortedArrays(self, X: List[int], Y: List[int]) -> float:
        if len(X) > len(Y):
            X, Y = Y, X
        
        # X is the smaller of the two
        # if X[-1] <= Y[0], whole array is sorted.
        # if Y[-1] <= X[0], whole array is sorted.
        half = (len(X) + len(Y) + 1) // 2 # for both even and odd case
        left, right = 0, len(X)
        while left <= right:
            part_x = (left + right) // 2
            part_y = half - part_x

            max_left_x = float('-inf') if part_x == 0 else X[part_x - 1]
            min_right_x = float('inf') if part_x == len(X) else X[part_x] 
            max_left_y = float('-inf') if part_y == 0 else Y[part_y - 1]
            min_right_y = float('inf') if part_y >= len(Y) else Y[part_y]
            # how do i know if the partion is correct
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # valid partition
                # all elements in the left partition are <= elements in the right partition.
                if (len(X) + len(Y)) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:
                # we have included too many elements from X
                right = part_x - 1
            else:
                # we should include more elements from X
                left = part_x + 1
        return None
