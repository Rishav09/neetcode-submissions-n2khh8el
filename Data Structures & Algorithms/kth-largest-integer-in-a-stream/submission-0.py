class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.streams = nums

    def add(self, val: int) -> int:
        self.streams.append(val)
        self.streams.sort(reverse=True)
        return self.streams[self.k-1]

        
