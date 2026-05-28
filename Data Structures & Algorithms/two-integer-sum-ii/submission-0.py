class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        while(l<r):
            cur_sum=nums[l]+nums[r]
            if(cur_sum==target):
                return [l+1,r+1]
            elif(cur_sum<target):
                l+=1
            else:
                r-=1
        return None