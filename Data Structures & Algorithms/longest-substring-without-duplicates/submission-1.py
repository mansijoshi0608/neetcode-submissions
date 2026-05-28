class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map={}
        l=0
        max_len=0
        for r in range(len(s)):
            if s[r] in hash_map:
                l=max(l,hash_map[s[r]]+1)
            hash_map[s[r]]=r
            max_len=max(r-l+1,max_len)
            

        return max_len
        