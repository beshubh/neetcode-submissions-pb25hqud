class Solution:
    def maximizeSweetness(self, sweetness: list[int], k: int) -> int:
        # minimum sweethness we can get
        left = min(sweetness)
        # maximume sweetness we can get
        right = sum(sweetness) // (
            k + 1
        )  # we have to divide the sweetness across k + 1 friends

        while left <= right:
            x = left + (right - left) // 2
            i = 0
            curr_sum = 0
            total_peices = 0
            while i < len(sweetness):
                curr_sum += sweetness[i]
                if curr_sum >= x:
                    # cut a piece
                    curr_sum = 0
                    total_peices += 1
                i += 1
            if total_peices >= k + 1:
                left = x + 1
            else:
                right = x - 1

        return left - 1
