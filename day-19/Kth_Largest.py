class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        target = len(nums) - k

        def quickSelect(left, right):
            if left == right:
                return nums[left]

            pivot = nums[(left + right) // 2]

            lt = left
            i = left
            gt = right

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1

                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1

                else:
                    i += 1

            if target < lt:
                return quickSelect(left, lt - 1)
            elif target > gt:
                return quickSelect(gt + 1, right)
            else:
                return nums[target]

        return quickSelect(0, len(nums) - 1)