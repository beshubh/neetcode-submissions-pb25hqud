
class TrieNode:

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end = False
        self.word = None

class PrefixTree:

    def __init__(self, root: TrieNode | None = None):
        self._root: TrieNode = root or TrieNode() 


    def insert(self, word: str) -> None:
        current = self._root
        for w in word:
            if w not in current.children:
                current.children[w] = TrieNode()
            current = current.children[w]
        current.is_end = True
        current.word = word

    def search(self, word: str) -> bool:
        current = self._root
        for w in word:
            if w not in current.children:
                return False
            current = current.children[w]
        return current.is_end

    def startsWith(self, prefix: str) -> bool:
        current = self._root
        for w in prefix:
            if w not in current.children:
                return False
            current = current.children[w]
        return True


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        result, visit = set(), set()
        root = TrieNode()
        index = PrefixTree(root)
        for word in words:
            index.insert(word) 
        def dfs(r: int, c: int, current: TrieNode):
            if current.is_end:
                result.add(current.word)
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[r]):
                return
            if (r, c) in visit:
                return
            char = board[r][c]
            visit.add((r, c))
            if char in current.children:
                new_root = current.children[char]
                dfs(r + 1, c, new_root)
                dfs(r - 1, c, new_root)
                dfs(r, c + 1, new_root)
                dfs(r, c - 1, new_root)
            visit.remove((r, c))
            
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] in root.children:
                    dfs(r, c, root)
        return list(result)
    














