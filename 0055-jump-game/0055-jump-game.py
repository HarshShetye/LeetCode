class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        f = 0
        for i in range(n):
            if i > f:
                return False
            f = max(f, i + nums[i])
        return True