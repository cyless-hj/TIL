class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        n = len(arr)

        if n % 2 == 1:
            answer = arr[n // 2]
        else:
            answer = (arr[n // 2] + arr[n // 2 - 1]) / 2
        return answer