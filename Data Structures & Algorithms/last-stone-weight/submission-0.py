class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesN = [-x for x in stones]
        heapq.heapify(stonesN) # O(n)

        while len(stonesN) > 1:
            first = -heapq.heappop(stonesN)
            second = -heapq.heappop(stonesN)

            if first != second:
                heapq.heappush(stonesN, -(first - second))
        if stonesN:
            return -stonesN[0]
        return 0