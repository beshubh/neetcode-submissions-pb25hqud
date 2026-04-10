
class PrefixTree:

    def __init__(self):
        self._store: set[str] = set()


    def insert(self, word: str) -> None:
        self._store.add(word)


    def search(self, word: str) -> bool:
        return word in self._store

    def startsWith(self, prefix: str) -> bool:
        for word in self._store:
            if word.startswith(prefix):
                return True
        return False
