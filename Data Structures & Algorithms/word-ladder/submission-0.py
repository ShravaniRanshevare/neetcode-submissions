class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        adj = defaultdict(list)
        for word in wordSet:
            for i in range(len(word)):
                pattern = word[:i]+ "*" + word[i+1:]
                adj[pattern].append(word)
                
        queue = deque([(beginWord,1)])
        visited = set([beginWord])
        
        while queue:
            word,level = queue.popleft()
            if word == endWord:
                return level
            
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                for nei in adj[pattern]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append([nei,level+1])
        return 0
               
                
        
            