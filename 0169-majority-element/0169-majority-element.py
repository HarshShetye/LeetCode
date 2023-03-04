import numpy as np
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        x = None
        for num in nums:
            if c == 0:
                x = num
            c += 1 if num == x else -1
        return x
