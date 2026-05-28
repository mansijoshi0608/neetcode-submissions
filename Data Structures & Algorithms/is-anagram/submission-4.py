class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        list1=[0]*26
        for letter in s:
            x = ord(letter) - ord('a')
            list1[x]+=1
        for letter in t:
            x = ord(letter) - ord('a')
            list1[x]-=1
        
        for i in range(0,26):
            if list1[i]!=0:
                return False
        return True
        


        


        