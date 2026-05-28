class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        l=0
        r=n-1
        res=[]
        for k in range(0,n):
            if(k==0 or nums[k-1]!=nums[k]):
                l=k+1
                r=n-1
                while(l<r):
                    sum1=nums[l]+nums[r]+nums[k]
                    if sum1==0:
                        res.append([nums[k],nums[l],nums[r]])
                        while l<r and nums[l+1]==nums[l]:
                            l+=1
                        while l<r and nums[r-1]==nums[r]:
                            r-=1
                        l+=1
                        r-=1
                    elif sum1>0:
                        r-=1
                    else:
                        l+=1
        return res
                
        