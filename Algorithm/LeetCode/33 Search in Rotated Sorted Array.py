class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
            
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[end] < nums[mid]:
                start = mid + 1
            else:
                end = mid
        
        pivot = start

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            r_pivot = (mid + pivot) % len(nums)
            if target == nums[r_pivot]:
                return r_pivot
            elif target < nums[r_pivot]:
                end = mid - 1
            else:
                start = mid + 1
        return -1