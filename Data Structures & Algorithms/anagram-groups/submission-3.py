class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ana={}
        for s in strs:
            sorted_s=''.join(sorted(s))
            if sorted_s not in dict_ana:
                dict_ana[sorted_s]=[s]
            else:
                dict_ana[sorted_s].append(s)
        res=[]
        for val in dict_ana.values():
            res.append(val)
        return res



            
        