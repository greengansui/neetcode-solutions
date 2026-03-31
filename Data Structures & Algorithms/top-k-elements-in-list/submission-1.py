class Solution:
    from collections import Counter
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) #Counter returns a dictionary; key as the element and the value as teh number of occurence
        heap = []
        result = []
        for key, value in count.items():
            heapq.heappush(heap, (-value,key))
        for i in range(k):
            value, key = heapq.heappop(heap)
            result.append(key)
        return result

            


        