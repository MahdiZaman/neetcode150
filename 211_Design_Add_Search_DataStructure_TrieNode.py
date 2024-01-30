class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.endofword = True

    # def search(self, word: str) -> bool:
    
        


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('abc')
# param_2 = obj.search(word)
print(obj.search('abc')) # Expected Output: True