class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map={}
        for n in nums:
            if n in count_map:
                count_map[n]+=1
            else:
                count_map[n]=1

        bucket = []
        n=len(nums)
        for i in range(n+1):
            bucket.append([])
        
        for key,value in count_map.items():
            bucket[value].append(key)
        res=[]
        for i in range(n,-1,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
        