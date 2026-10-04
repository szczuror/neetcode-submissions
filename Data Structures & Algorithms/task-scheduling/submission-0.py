class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycles = 0

        heap = [0 for _ in range(26)]
        for task in tasks:
            heap[ord(task) - ord('A')] -= 1 # cause of it being a min heap later and we want a max heap
        heap = [f for f in heap if f < 0]
        heapq.heapify(heap)

        q = deque()

        while heap or q:
            cycles += 1

            if heap:
                curr = heapq.heappop(heap) + 1
                if curr < 0:
                    q.append((curr, cycles + n))
            if q and q[0][1] == cycles:
                heapq.heappush(heap, q.popleft()[0])
        
        return cycles