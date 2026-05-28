
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        dict1={}
        res=[]
        for i in nums:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        
        for key,val in dict1.items():
            heapq.heappush(heap,(-val,key))

        for i in range(k):
            if len(heap)>0:
                res.append(heapq.heappop(heap)[1])
        
        return res