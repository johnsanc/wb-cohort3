class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        words_in_board = []
        trie = self.Trie()
        node_pointer = trie.root
        
        for word in words:
            trie.insert(word)
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.dfs(node_pointer, r, c, board, words_in_board, "")
        
        return words_in_board
    
    def dfs(self, node_pointer, r, c, board, result, builder):
        if node_pointer.end:
            result.append(builder)
            node_pointer.end = False
        
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            return
        
        # Make copy of current letter
        temp = board[r][c]
        
        # Get the next pointer
        node_pointer = node_pointer.children.get(temp)
        
        if not node_pointer:
            return
        
        board[r][c] = '#'
        self.dfs(node_pointer, r + 1, c, board, result, builder + temp)
        self.dfs(node_pointer, r - 1, c, board, result, builder + temp)
        self.dfs(node_pointer, r, c + 1, board, result, builder + temp)
        self.dfs(node_pointer, r, c - 1, board, result, builder + temp)
        board[r][c] = temp
        
        
        
    
    class Trie:
        
        class TrieNode:    
            def __init__(self):
                self.children = collections.defaultdict()
                self.end = False
                
        def __init__(self):
            self.root = self.TrieNode()
            
        def insert(self, word):
            root = self.root
            
            for l in word:
                if l not in root.children:
                    root.children[l] = self.TrieNode()
                root = root.children.get(l)
            
            root.end = True