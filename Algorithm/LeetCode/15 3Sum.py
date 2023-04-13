from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        if nums[0] > 0 or nums[-1] < 0:
            return []

        answer = []
        for i in range(len(nums) - 2):
            start, end = i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while start < end:
                sum = nums[i] + nums[start] + nums[end]

                if sum == 0:
                    answer.append([nums[i], nums[start], nums[end]])
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    start += 1
                    end -= 1
                elif sum > 0:
                    end -= 1
                else:
                    start += 1

        return answer