class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0 
        r=len(nums)-1
        while(l<r):
            cur_sum=nums[l]+nums[r]
            if target == cur_sum:
                return [l+1,r+1]
            elif target < cur_sum:
                r=r-1
            else:
                l=l+1
        return [-1,-1]