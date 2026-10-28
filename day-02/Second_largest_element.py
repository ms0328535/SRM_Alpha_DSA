
class Solution:
    def secondLargest(self, nums: list[int]) -> int:
        largest = float('-inf')
        second = float('-inf')

        for num in nums:
            if num >= largest:
                second = largest
                largest = num
            elif num > second:
                second = num

        return second
