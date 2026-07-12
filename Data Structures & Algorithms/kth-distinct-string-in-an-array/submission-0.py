class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dis = collections.Counter(arr)
        l = [ key for key in dis if dis[key] == 1]
        #we have all d and thier order
        if k > len(l):
            return ""
        return l[k-1]