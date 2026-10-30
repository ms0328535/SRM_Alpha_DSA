
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        num_set = set(nums)
        longest = 0

        for num in num_set:

            # Check whether it is the starting number
            if num - 1 not in num_set:

                current = num
                count = 1

                # Count consecutive numbers
                while current + 1 in num_set:
                    current += 1
                    count += 1

                if count > longest:
                    longest = count

        return longest
