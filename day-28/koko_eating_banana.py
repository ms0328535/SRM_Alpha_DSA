class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        def canEat(speed):
            hours = 0

            for pile in piles:
                hours += (pile + speed - 1) // speed

            return hours <= h

        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2

            if canEat(mid):
                right = mid
            else:
                left = mid + 1

        return left