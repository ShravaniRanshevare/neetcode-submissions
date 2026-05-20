class PrefixTree:

    def __init__(self):
        self.tree=[]

    def insert(self, word: str) -> None:
        self.tree.append(word)

    def search(self, word: str) -> bool:
        if word in self.tree:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        for w in self.tree:
            if w.startswith(prefix):
                return True
            
        return False
        