class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        flag=False
        count=0
        visited = set()
        def helper(i,j,visited: set,count):
            if count == len(word):
                return True
            if i< 0 or i>=len(board) or j<0 or j>= len(board[i]):
                return False
           
            cell = board[i][j]
            if cell == word[count] and (i,j) not in visited:
                visited.add((i,j))
                four = [(0,1),(0,-1),(1,0),(-1,0)]
                for di,dj in four:
                    if helper(i+di,j+dj,visited,count+1):
                        return True
                visited.remove((i,j))
            else:
                return False
                
        for i in range(len(board)) :
            for j in range(len(board[i])):  
                flag = helper(i,j,visited,count)
                if flag:
                    return True
        return False
        
                    
                        
