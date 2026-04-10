
INF = float('inf')


class Solution:
    def findMedianSortedArrays(self, X: List[int], Y: List[int]) -> float:
        if len(X) > len(Y):
            X, Y = Y, X
        half = (len(X) + len(Y) + 1) // 2 # handle odd length cases.
        l, r = 0, len(X)
        while l <= r:
            part_x = (l + r) // 2 # total elements included from X
            part_y = half - part_x # total elements included from Y
            max_left_x = -INF if part_x - 1 < 0 else X[part_x - 1]
            min_right_x = INF if part_x >= len(X) else X[part_x]

            max_left_y = -INF if part_y - 1 < 0 else Y[part_y - 1]
            min_right_y = INF if part_y >= len(Y) else Y[part_y]

            # found
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (len(X) + len(Y)) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                return max(max_left_x, max_left_y)
            # to left
            if max_left_x > min_right_y:
                r = part_x - 1
            else:
                l = part_x + 1
