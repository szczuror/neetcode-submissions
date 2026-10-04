class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # k closests points to 0,0.
        # euclidean distance
        def distToOrigin(point: List[int]) -> int:
            return ((point[0]**2 + point[1]**2))
        
        heap = []
        heapq.heapify(heap)

        for point in points:
            heapq.heappush(heap, (-distToOrigin(point), point))
            if len(heap) > k:
                heapq.heappop(heap)

        return [p for _,p in heap]

        # heap = [(p[0]**2 + p[1]**2, p) for p in points]

        # heapq.heapify(heap)

        # return [heapq.heappop(heap)[1] for _ in range(k)]