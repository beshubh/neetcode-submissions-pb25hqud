INF = float('inf')

class Solution:
    def findMedianSortedArrays(self, X: List[int], Y: List[int]) -> float:
        if len(X) > len(Y):
            X, Y = Y, X
        
        left, right = 0, len(X)
        half = (len(X) + len(Y) + 1) // 2 # +1 so odd/even both can be handled | 2
        while left <= right: # 0 <= 2
            mid = (left + right) // 2 # number of elements in the left partition | 1
            part_x = mid  # 1
            part_y = half - mid # 2 - 1 => 1
            # maximum from the left partition of X
            # as part_x is number of elements from the left partiton, that means maximum should 
            # be at part_x - 1 (index)
            max_left_x = -INF if part_x <= 0 else X[part_x - 1] # 3

            # minium from the right partition of X
            min_right_x = INF if part_x >= len(X) else X[part_x] # INF

            # maximum from the left partition of Y
            max_left_y = -INF if part_y <= 0 else Y[part_y - 1] # 1
            # minimum from the right parttion of Y
            min_right_y = INF if part_y >= len(Y) else Y[part_y] # 2

            # found the target iff
            # maximum from the left of X is smaller than minimum from right of Y and
            # maximum from the left of Y is smaller than minimum from right of X as
            # left of both X and Y are smaller than their rights, if we can prove that
            # both lefts are smaller than opposite's rights as well that means we can partition this 
            # array at this point
            if max_left_x <= min_right_y and max_left_y <= min_right_x: # 3 <= 2 and 1 <= INF
                # even case
                print('max left x', max_left_x, 'max_left_y', max_left_y)
                if (len(X) + len(Y)) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                # odd case
                return max(max_left_x, max_left_y)
            
            # go to the left, if we have included way too many elements from X
            if max_left_x > min_right_y:
                right = mid - 1
            else:
                left = mid + 1
        return None
