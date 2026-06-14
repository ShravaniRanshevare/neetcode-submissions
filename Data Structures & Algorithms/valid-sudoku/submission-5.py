class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(len(board)):
            seen=set()
            for i in range(len(board[row])):
                if board[row][i] == ".":
                    continue
                if board[row][i] not in seen:
                    seen.add(board[row][i])
                else:
                    return False
        
        
        for col in range(9):
            seen=set()
            for i in range(9):
                e= board[i][col]
                if e == ".":
                    continue
                if e not in seen:
                    seen.add(e)
                else:
                    return False
        

        
        for sq in range(9):
            seen = set()
            for i in range(3): #each cell in 3x3 since thats virtual these indices wont work hence row and col
                for j in range(3):
                    row = (sq//3)*3 + i #row it belongs to
                    col = (sq % 3)*3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] not in seen:
                        seen.add(board[row][col])
                    else:
                        return False
        
        return True 

                    

        
        

        
