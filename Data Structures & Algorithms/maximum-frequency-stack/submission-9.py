import collections


class FreqStack:
    def __init__(self):
        self._freq = collections.defaultdict(int)
        self._groups: dict[int, list] = {}
        self._max_freq: int = 0

    def push(self, val: int) -> None:
        self._freq[val] += 1
        val_freq = self._freq[val]
        if self._max_freq < val_freq:
            self._max_freq = val_freq
        if val_freq not in self._groups:
            self._groups[val_freq] = [val]
        else:
            self._groups[val_freq].append(val)

    def pop(self) -> int:
        result = self._groups[self._max_freq].pop()
        self._freq[result] -= 1
        while (
            (self._max_freq not in self._groups) or len(self._groups[self._max_freq]) == 0
        ):
            if self._max_freq == 0:
                break
            self._max_freq -= 1
        return result


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
