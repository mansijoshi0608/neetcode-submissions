class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i not in map1:
                map1[i]=1
            else:
                map1[i]+=1
        for i in t:
            if i not in map1 or map1[i]<=0:
                return False
            else :
                map1[i]-=1
        return True
        