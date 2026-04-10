
class TrieNode:

    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end = False
        self.full_word = ''

class PrefixTrie:

    def __init__(self, root: TrieNode | None = None):
        self.root = root or TrieNode()
    
    def insert(self, word: str):
        current = self.root
        for w in word:
            if w not in current.children:
                current.children[w] = TrieNode()
            current = current.children[w]
        current.full_word = word
        current.is_end = True
    
    def search(self, word: str) -> bool:
        current = self.root
        for w in word:
            if w not in current.children:
                return False
            current = current.children[w]
        return current.is_end

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        trie = PrefixTrie(root)
        ROWS, COLS = len(board), len(board[0])
        for word in words:
            trie.insert(word)

        visit = set() 
        output = []
        def find_words(r: int, c: int, root):
            if root.is_end:
               output.append(root.full_word)
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            if (r, c) in visit:
                return
            visit.add((r, c))
            w = board[r][c]
            if w in root.children:
                new_root = root.children[w]
                find_words(r + 1, c, new_root)
                find_words(r - 1, c, new_root)
                find_words(r, c + 1, new_root)
                find_words(r, c - 1, new_root)
            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                w = board[r][c]
                if w in root.children:
                    find_words(r, c, root)
        return list(set(output))
