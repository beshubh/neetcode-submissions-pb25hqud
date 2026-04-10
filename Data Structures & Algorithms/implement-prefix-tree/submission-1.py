
class PrefixTree:

    def __init__(self):
        self._store: set[str] = set()
        self._tree = {}


    def insert(self, word: str) -> None:
        self._store.add(word)
        node = self._tree
        for w in word:
            if w not in node:
                node[w] = {}
                node = node[w]
            else:
                node = node[w]
        print(self._tree)

    def search(self, word: str) -> bool:
        return word in self._store

    def startsWith(self, prefix: str) -> bool:
        node = self._tree
        for w in prefix:
            if w not in node:
                return False
            node = node[w]
        return True
