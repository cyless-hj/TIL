class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1

        while start < end < len(numbers):
            tmp = numbers[start] + numbers[end]
            if tmp < target:
                start += 1
            elif tmp > target:
                end -= 1
            else:
                return [start + 1, end + 1]