class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            i = ord(c)-ord("a")
            if current.children[i] == None:
                current.children[i] = TrieNode()
            current = current.children[i]
        current.end = True
        
    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            i = ord(c)-ord("a")
            if current.children[i] == None:
                return False
            current = current.children[i]
        return current.end

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            i = ord(c)-ord("a")
            if current.children[i] == None:
                return False
            current = current.children[i]
        return True