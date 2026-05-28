class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        hashtable=[0]*26
        for i in range(len(s)):
            index1=ord(s[i])-ord('a')
            index2=ord(t[i])-ord('a')
            hashtable[index1]+=1
            hashtable[index2]-=1

        for i in range(0,26,1):
            if hashtable[i]!=0:
                return False
        return True
        
        
        