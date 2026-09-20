class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        piles_n = len(piles)

        left, right = 1, k

        bestK = right

        while left <= right:
            currK = (left + right) // 2

            total_hours = 0
            for p in piles:
                total_hours += (p + currK - 1) // currK
                if total_hours > h:
                    break

            if total_hours <= h:
                bestK = currK
                right = currK - 1
            else:
                left = currK + 1


        return bestK