class MinStack:

    def __init__(self):
        self._store = []
        self._prefix_min = []

    def push(self, val: int) -> None:
        self._store.append(val)
        if not self._prefix_min:
            self._prefix_min.append(val)
        else:
            self._prefix_min.append(min(self._prefix_min[-1], val))

    def pop(self) -> None:
        self._store.pop()
        self._prefix_min.pop()

    def top(self) -> int:
        return self._store[-1]

    def getMin(self) -> int:
        return self._prefix_min[-1]

        
