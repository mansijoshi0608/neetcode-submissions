
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]
        dict1={}
        res=[]
        for i in nums:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1

        for key,val in dict1.items():
            bucket[val].append(key)

        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res
        
        
        
        return res