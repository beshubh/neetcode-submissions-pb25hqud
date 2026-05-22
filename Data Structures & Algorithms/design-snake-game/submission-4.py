import collections


class SnakeGame:
    DIR_UP = (-1, 0)
    DIR_DOWN = (1, 0)
    DIR_RIGHT = (0, 1)
    DIR_LEFT = (0, -1)


    def __init__(self, width: int, height: int, food: List[List[int]]):
        self._height = height
        self._widht = width
        self._board = [[0 for _ in range(width)] for _ in range(height)]
        self._current_location = (0, 0)
        self._current_score = 0
        self._snake_locations = collections.deque([(0, 0)])
        self._snake_locations_set = set([(0, 0)])
        self._food = collections.deque([tuple(f) for f in food])
    
    def _get_next_location(self, direction: tuple[int, int]) -> tuple[int, int]:
        return (self._current_location[0] + direction[0], self._current_location[1] + direction[1])
    
    def _out_of_bounds(self, r, c) -> bool:
        if r < 0 or r >= self._height or c < 0 or c >= self._widht:
            return True
        return False

    def move(self, direction: str) -> int:
        match direction:
            case 'R':
                next_location = self._get_next_location(self.DIR_RIGHT) 
            case 'D':
                next_location = self._get_next_location(self.DIR_DOWN) 
            case 'L':
                next_location = self._get_next_location(self.DIR_LEFT) 
            case 'U':
                next_location = self._get_next_location(self.DIR_UP) 
            case _:
                raise ValueError('Invaid locaton')
        r, c = next_location
        if self._out_of_bounds(r, c):
            return -1
        
        if self._food and (r, c) == self._food[0]:
            self._current_score += 1
            if next_location in self._snake_locations_set:
                return -1
            self._food.popleft()
            self._snake_locations.append(next_location)
            self._snake_locations_set.add(next_location)
        else:
            x = self._snake_locations.popleft()
            self._snake_locations_set.remove(x)
            if next_location in self._snake_locations_set:
                return -1
            self._snake_locations.append(next_location)
            self._snake_locations_set.add(next_location)

        self._current_location = next_location

        return self._current_score  




        



        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
