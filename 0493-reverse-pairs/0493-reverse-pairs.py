class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(l, r):
            if l >= r:
                return 0
            mid = (l + r) // 2
            count = mergeSort(l, mid) + mergeSort(mid + 1, r)
            i, j = l, mid + 1
            while i <= mid and j <= r:
                if nums[i] > 2 * nums[j]:
                    count += mid - i + 1
                    j += 1
                else:
                    i += 1
            nums[l:r+1] = sorted(nums[l:r+1])
            return count

        return mergeSort(0, len(nums) - 1)