class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # using window + min would be O(n^2) tho

        # window of a fixed size k, create a (priority?) heap to remember curr maxs
        heap = []
        res = []
        n = len(nums)

        for i, val in enumerate(nums):
            heapq.heappush(heap, (-val, i))

            while heap[0][1] <= i - k: # we throw out not matchin vals
                heapq.heappop(heap)
            
            # then we take a peek at the current max val

            res.append(-heap[0][0])

        return res[k - 1:]

            