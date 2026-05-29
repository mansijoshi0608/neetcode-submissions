class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:

        n=len(temp)
        res = [0] * n
        stack = []
        for i in range(n):
            # While stack is not empty and current temp is warmer than the temp at the top of the stack
            while stack and temp[i] > temp[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)
        return res




