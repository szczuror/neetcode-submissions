class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.target = k
        self.heap = nums

        heapq.heapify(self.heap)
        # cut to k elems

        while len(self.heap) > k:
            heapq.heappop(self.heap) 

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.target:
            heapq.heappop(self.heap)
        return self.heap[0]