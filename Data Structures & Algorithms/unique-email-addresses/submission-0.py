class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        sent = set()
        #go thru each and every email
        #first edit it ie if encounter a period keep it adding it but if u encounter + skip till@ occurs
        # if its not in sent already add it
        # return len(sent)
        for e in emails:
            res = ""
            end= ""
            for c in range(len(e)):
                if e[c] == ".":
                    continue
                if e[c] == "+":
                    i=c
                    while e[i] != "@":
                        i += 1
                    end = e[i:]
                    break 
                else:
                    res = res + e[c]
            final = res + end
            if final not in sent:
                sent.add(final)
        print(sent)
        return len(sent)
            
