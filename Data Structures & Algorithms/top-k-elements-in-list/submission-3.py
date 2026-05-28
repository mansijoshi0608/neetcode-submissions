class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        for n in nums:
            if n not in dict1:
                dict1[n]=1
            else:
                dict1[n]+=1
        sorted_items=dict(sorted(dict1.items(), key=lambda item: item[1],reverse=True))
        res=[]
        for key,value in sorted_items.items():
            if k>0:
                res.append(key)
                k-=1
            else:
                break
        return res

