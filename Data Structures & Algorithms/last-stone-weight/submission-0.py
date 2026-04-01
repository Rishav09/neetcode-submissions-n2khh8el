import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap) # O(n)

        while len(heap) > 1:
            y_neg = heapq.heappop(heap) # O(log N)
            x_neg = heapq.heappop(heap) # O(log N)

            if y_neg < x_neg:
                diff_neg = y_neg - x_neg
                heapq.heappush(heap, diff_neg) # O(logN)

        if len(heap) == 0:
            return 0
        else:
            return -heap[0]