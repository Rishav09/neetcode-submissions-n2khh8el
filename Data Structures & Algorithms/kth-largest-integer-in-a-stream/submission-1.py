

import heapq



class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        # Store k and initialize the min-heap
        self.k = k
        self.heap = []
        # We don't need to explicitly heapify an empty list

        # Process the initial numbers using the add logic
        # This ensures the heap is correctly built and potentially trimmed
        # right from the start.
        for num in nums:
            self.add(num) # Call the object's own add method

    def add(self, val: int) -> int:
        # This method adds 'val' to the stream and returns the kth largest.

        # Case 1: Heap hasn't reached size k yet.
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            # If after adding, the heap size is now exactly k,
            # the root is the kth largest. If less than k, the root is the
            # smallest element among those seen, which fits the definition
            # in progress. So self.heap[0] works here too after push.

        # Case 2: Heap is already full (size k).
        # We only care if the new value is larger than the smallest
        # element currently in the heap (which is the kth largest overall).
        elif val > self.heap[0]:
             # If val is larger, it replaces the smallest element in the heap.
             # heapreplace pops the smallest (self.heap[0]) and pushes val,
             # then re-heapifies. More efficient than separate pop/push.
            heapq.heapreplace(self.heap, val)

        # The kth largest element is always the minimum element in our
        # min-heap of size k (or less than k if not enough elements seen).
        # The check 'val > self.heap[0]' ensures we only replace when needed.
        # If val <= self.heap[0] and heap size is k, we do nothing,
        # and the kth largest remains self.heap[0].

        # Return the current kth largest element, which is the root of the min-heap.
        # Note: This assumes k >= 1. If k=0, this class wouldn't make sense.
        # Also, the problem implies we want the kth largest. If fewer than
        # k elements exist *total*, what should be returned? The problem
        # statement implicitly suggests add() is called until at least k
        # elements might be present, or the initial nums fills it.
        # Returning self.heap[0] seems the most consistent interpretation.
        return self.heap[0]

        
