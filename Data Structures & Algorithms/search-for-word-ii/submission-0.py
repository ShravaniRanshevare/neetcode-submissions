class Trie:
    def __init__(self):
        self.trie = {}
        self.children= self.trie.keys() 
    def insert(self, word: str,i) -> None:
        node = self.trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['index'] = i
        node['#'] = True   # end marker

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return '#' in node
            ch = word[i]
            if ch == '.':  # wildcard
                for child in node:
                    if child != '#' and dfs(node[child], i+1):
                        return True
                return False
            if ch not in node:
                return False
            return dfs(node[ch], i+1)
        
        return dfs(self.trie, 0)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        
        res = []
        for i in range(len(words)):
            trie.insert(words[i],i)
        
        def backtrack(i,j,node):
            if i<0 or i>=len(board) or j<0 or j>=len(board[i]):
                return False
            
            cell = board[i][j]
            if cell in node:
                node=node[cell]
                if "#" in node:
                    res.append(words[node["index"]])
                    node.pop("#")
                board[i][j] = "#"
                four = [(-1,0),(0,-1),(0,1),(1,0)]
                for di,dj in four:
                    backtrack(i+di,j+dj,node)
                board[i][j]= cell
            else:
                return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                backtrack(i,j,node=trie.trie)

        return res
