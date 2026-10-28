class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:

        def canShip(capacity):
            total = 0
            need = 1

            for weight in weights:
                if total + weight > capacity:
                    need += 1
                    total = 0
                total += weight

            return need <= days

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2

            if canShip(mid):
                right = mid
            else:
                left = mid + 1

        return left