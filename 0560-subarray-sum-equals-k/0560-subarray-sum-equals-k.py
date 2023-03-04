class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:    
        c,s = 0,0
        s_map = {0: 1}
        for i in nums:
            s += i
            if s - k in s_map:
                c += s_map[s - k]
            if s in s_map:
                s_map[s] += 1
            else:
                s_map[s] = 1
        return c