class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            slot1_start, slot1_end = slots1[i]
            slot2_start, slot2_end = slots2[j]

            # is there a valid slot?
            if slot2_start >= slot1_end:
                i += 1
                continue
            print('slot1: ', slot1_start, slot1_end)
            print('slot2: ', slot2_start, slot2_end)
            print('*-------*')
            diff1 = slot1_end - slot1_start
            diff2 = slot2_end - slot2_start

            start = max(slot1_start, slot2_start)
            end = min(slot1_end, slot2_end)
            if end - start >= duration:
                return [start, start + duration]
            elif diff1 < diff2:
                i += 1
            else:
                j += 1
        return []
            


