class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        l=0
        r=n-1
        max_vol=0
        while(l<r):
            width=r-l
            max_vol=max(max_vol,min(heights[l],heights[r])*width )

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1


        return max_vol

        