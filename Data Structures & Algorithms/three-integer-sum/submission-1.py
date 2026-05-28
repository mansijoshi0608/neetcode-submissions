class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        n=len(nums)
        for i in range(n-1):
            l=i+1
            r=n-1
            if(i==0 or nums[i-1]!=nums[i]):
                while(l<r):
                    target=nums[l]+nums[r]+nums[i]
                    if(target==0):
                        res.append([nums[i],nums[l],nums[r]])
                        while l<r and nums[l+1]==nums[l]:
                            l+=1
                        while l<r and nums[r-1]==nums[r]:
                            r-=1
                        l+=1
                        r-=1
                    elif target < 0:
                        l+=1
                    else: 
                        r-=1
        
        return res
