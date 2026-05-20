class WordDictionary:

    def __init__(self):
        self.words = dict()

    def addWord(self, word: str) -> None:
        node=self.words
        for ch in word:
            if ch not in node:
                node[ch]= dict()
            node = node[ch]
        node['#'] = True

    def search(self, word: str) -> bool:
        def dfs(node,i):
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
        
        return dfs(self.words, 0)  
