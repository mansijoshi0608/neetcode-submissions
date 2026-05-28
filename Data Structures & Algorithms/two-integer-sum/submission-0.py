class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set1={}
        for i in range(len(nums)):
            if target-nums[i] in set1:
                return [set1[target-nums[i]],i]
            set1[nums[i]]=i
        return -1
        