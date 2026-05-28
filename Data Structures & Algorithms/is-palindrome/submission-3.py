class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        n=len(s)
        while(l<r):
            while l<n and not s[l].isalnum():
                l+=1
            while r>=0 and  not s[r].isalnum():
                r-=1
            if l<n  and  r>=0 and s[l].lower()==s[r].lower():
                l+=1
                r-=1
            elif  l<n  and  r>=0 and s[l].isalnum() and s[r].isalnum() and s[l]!=s[r]:
                print(l,r,s[l],s[r])
                return False

        return True

        