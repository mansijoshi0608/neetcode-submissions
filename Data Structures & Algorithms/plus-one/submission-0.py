class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=[]
        n=len(digits)
        carry=1
        for i in range(n-1,-1,-1):
            sum1=digits[i]+carry
            if sum1>9:
                carry=1
                sum1=sum1%10
            else: 
                carry=0

            res.append(sum1)
        if carry:
            res.append(carry)
        res.reverse()
        return res

        