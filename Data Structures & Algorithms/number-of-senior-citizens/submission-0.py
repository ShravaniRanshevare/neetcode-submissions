class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        #indices r 0-14
        #indice 11-12 = age
        for d in details:
            if int(d[11:12+1]) > 60:
                count += 1
        return count 