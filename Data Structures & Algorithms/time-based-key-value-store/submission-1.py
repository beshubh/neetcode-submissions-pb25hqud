import collections
import unittest


ValueStruct = collections.namedtuple('ValueStruct', ['ts', 'val'])

class TimeMap:

    def __init__(self):
        self._store: dict[str, list[ValueStruct]] = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        entry = self._store[key]
        entry.append(ValueStruct(timestamp, value))
    

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._store:
            return ''
        
        val_structs = self._store[key]
        value = self._bin_search(target_ts=timestamp, val_structs=val_structs)
        return value
    
    def _bin_search(self, target_ts: int, val_structs: list[ValueStruct]) -> str:
        left, right = 0, len(val_structs) - 1
        potential = ''
        while left <= right:
            mid = left + ((right - left) // 2)
            ts_at_mid = val_structs[mid].ts
            if target_ts > ts_at_mid:
                potential = val_structs[mid].val
                left = mid + 1
            elif target_ts < ts_at_mid:
                right = mid - 1
            else:
                return val_structs[mid].val
        return potential
