class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2=len(s1),len(s2)

        if n1>n2:
            return False

        s1_map=[0]*26
        s2_map=[0]*26 

        for i in range(n1):
            ele_s1=ord(s1[i])-ord('a')
            ele_s2=ord(s2[i])-ord('a')
            s1_map[ele_s1]+=1
            s2_map[ele_s2]+=1
        if s1_map==s2_map:
            return True
        for i in range(n1,n2):
            ele_s2=ord(s2[i])-ord('a')
            s2_map[ord(s2[i-n1])-ord('a')]-=1
            s2_map[ele_s2]+=1
            if s1_map==s2_map:
                return True

        return False


             