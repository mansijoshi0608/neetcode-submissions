class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i in range(len(nums)):
            missing_no=target-nums[i] 
            if missing_no in dict1:
                return [dict1[missing_no],i]
            dict1[nums[i]]=i
        return[-1,-1]