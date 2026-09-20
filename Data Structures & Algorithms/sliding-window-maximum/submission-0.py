class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # nlogn time. So sorting is involved i guess? or binsearch
        # using window + min would be O(n^2) tho
        # using queue to save current min? and popping from the left when a current apperas
        # like in this system design question before

        # window of a fixed size k, create a (priority?) heap to remember curr mins
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

            