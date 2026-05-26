

class Leaderboard:

    def __init__(self):
        self._players = {}       

    def addScore(self, playerId: int, score: int) -> None:
        self._players[playerId] = self._players.get(playerId, 0) + score

    def top(self, K: int) -> int:
        return sum(sorted(self._players.values(), reverse=True)[:K])

    def reset(self, playerId: int) -> None:
        self._players[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
