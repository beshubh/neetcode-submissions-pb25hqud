

class TurnStile:
    ENTER = 0
    EXIT = 1

    def __init__(self, arrival: list[int], state: list[int]) -> None:
        self._clock = 0
        self._cur = 0
        self._enter = deque()
        self._exit = deque()
        self._used_prev_second = False
        self._prev_direction = self.EXIT
        self._arrival = arrival
        self._output = [-1]*len(arrival)
        self._state = state
    
    def _add_arrivals(self):
        while self._cur < len(self._arrival) and self._arrival[self._cur] <= self._clock:
            if self._state[self._cur] == self.ENTER:
                self._enter.appendleft(self._cur)
            else:
                self._exit.appendleft(self._cur)
            self._cur += 1

    def _choose_direction(self):
        prefer = self._prev_direction if self._used_prev_second else self.EXIT
        if prefer == self.EXIT and self._exit:
            return self.EXIT
        if prefer == self.ENTER and self._enter:
            return self.ENTER
        return self.ENTER if prefer == self.EXIT else self.EXIT

    def step(self):
        self._add_arrivals()
        if not self._enter and not self._exit:
            if self._cur == len(self._arrival):
                return False
            self._clock += 1
            self._used_prev_second = False
            return True
        dir = self._choose_direction()
        if dir == self.ENTER:
            person = self._enter.pop()
        else:
            person = self._exit.pop()
        self._output[person] = self._clock
        self._clock += 1
        self._used_prev_second = True
        self._prev_direction = dir
        return True
    
    def run(self):
        while self.step():
            pass
        return self._output


class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        return TurnStile(arrival, state).run()
