from collections import defaultdict
class Trie:
    class TrieNode:
        def __init__(self):
            self.children = defaultdict()
            self.end = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.get_node()
    
    def get_node(self):
        return self.TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        word_length = len(word)
        
        for i in range(word_length):
            letter_index = self.calc_index(word[i])
            
            if letter_index not in root.children:
                root.children[letter_index] = self.get_node()
                
            root = root.children.get(letter_index)
        
        root.end = True
    
    def calc_index(self, c):
        return ord(c) - ord('a')
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        word_length = len(word)
        
        for i in range(word_length):
            letter_index = self.calc_index(word[i])
            
            if letter_index not in root.children:
                return False
        
            root = root.children.get(letter_index) # progress the pointer
            
        if root.end:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        prefix_length = len(prefix)
        root = self.root
        
        for i in range(prefix_length):
            letter_index = self.calc_index(prefix[i])
            
            if letter_index not in root.children:
                return False
            
            root = root.children.get(letter_index)
            
        # return true since we either can move forward if root.end is False or if
        # prefix = word, root.end = True.
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)