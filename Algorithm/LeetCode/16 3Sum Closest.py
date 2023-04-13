class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        answer = int(1e9)
        nums.sort()

        for i in range(len(nums) - 2):
            start, end = i + 1, len(nums) - 1
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if abs(target - sum) < abs(answer):
                    answer = target - sum
                if sum > target:
                    end -= 1
                else:
                    start += 1
            if answer == 0:
                break
        return target - answer