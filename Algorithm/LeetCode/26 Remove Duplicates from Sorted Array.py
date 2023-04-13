class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        answer = 0
        for i in range(1, len(nums)):
            if nums[answer] != nums[i]:
                answer += 1
                nums[answer], nums[i] = nums[i], nums[answer]
        return answer + 1