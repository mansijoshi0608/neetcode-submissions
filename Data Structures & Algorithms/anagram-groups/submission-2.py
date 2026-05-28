class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_s={}
        for s in strs:
            sorted_s=''.join(sorted(s))
            if sorted_s not in dict_s:
                dict_s[sorted_s]=[s]
            else:
                dict_s[sorted_s].append(s)

        result_list=[]
        for k,v in dict_s.items():
            result_list.append(v)
        return result_list
        

        