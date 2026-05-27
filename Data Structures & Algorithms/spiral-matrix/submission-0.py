class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        main=[]
        if not matrix:
            return main
        top=0
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1

        while top <= bottom and left<=right:
            for l in range(left,right+1):
                main.append(matrix[top][l])
            top +=1
            for j in range(top,bottom+1):
                main.append(matrix[j][right])
            right -= 1
            if top<=bottom:
                for s in range(right,left-1,-1):
                    main.append(matrix[bottom][s])
                bottom -= 1
            if left<=right:
                for t in range(bottom,top-1,-1):
                    main.append(matrix[t][left])
                left += 1
        return main


