class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1={}
        n=len(nums)
        for i in range(0,n):
            x=target-nums[i]
            if x in map1:
                return [map1[x],i]
            map1[nums[i]]=i
        return [-1,-1]

        