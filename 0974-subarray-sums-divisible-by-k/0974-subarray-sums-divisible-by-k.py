from collections import defaultdict 
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        a = 0
        b = defaultdict(int)
        b[0] = 1
        for i in nums:
            a = (a + i) % k
            count += b[a]
            b[a] += 1
        return count