
class PrefixTree:

    def __init__(self):
        self._tree = {}


    def insert(self, word: str) -> None:
        node = self._tree
        for w in word:
            if w not in node:
                node[w] = {}
                node = node[w]
            else:
                node = node[w]
        node['is_end'] = True

    def search(self, word: str) -> bool:
        node = self._tree
        for w in word:
            if w not in node:
                return False
            node = node[w]
        return node.get('is_end', False) or False 

    def startsWith(self, prefix: str) -> bool:
        node = self._tree
        for w in prefix:
            if w not in node:
                return False
            node = node[w]
        return True
