"""
Problem: Top K Frequent Elements
LeetCode: https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements.
"""

from typing import List
from collections import defaultdict
import heapq

# -----------------------------------------------------------
# 📘 Approach 1: Bucket Sort (Optimal)
# 
# ✅ Logic:
# - Count the frequency of each number using a hash map.
# - Use the bucket sort algorithm to create n+1 buckets.
#   Each bucket at index i stores the numbers that appear i times.
# - Traverse buckets in reverse order (from high freq to low),
#   collecting elements until we have k most frequent.
#
# Time: O(n)       — One pass to count, one to bucket, one to collect top k
# Space: O(n)      — Hash map + buckets + result list
# -----------------------------------------------------------

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}  # num -> frequency
        buckets = [[] for _ in range(len(nums) + 1)]  # buckets[i] holds nums with frequency i
        res = []

        # Step 1: Count frequency of each number
        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)

        # Step 2: Group numbers by frequency using bucket sort
        for num, freq in freqMap.items():
            buckets[freq].append(num)

        # Step 3: Traverse buckets in reverse to collect k most frequent numbers
        for i in range(len(buckets) - 1, 0, -1):
            for number in buckets[i]:
                res.append(number)
                if len(res) == k:
                    return res
        
        return res  # fallback if input is invalid (e.g., k > len(nums))

# -----------------------------------------------------------
# 🧪 Example:
# Input: nums = [1,1,1,2,2,3], k = 2
# Step 1: freqMap = {1: 3, 2: 2, 3: 1}
# Step 2: buckets = [
#     [],        # 0 times
#     [3],       # 1 time
#     [2],       # 2 times
#     [1],       # 3 times
#     [], [], ...] (up to len(nums) + 1)
# Step 3: Traverse buckets from right to left → [1, 2]
# Output: [1, 2]
# -----------------------------------------------------------

# -----------------------------------------------------------
# 📘 Approach 2: Min-Heap (Not optimal)
# Push frequencies into a min-heap of size k.
# Time: O(n log k)
# Space: O(n)
# -----------------------------------------------------------

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


# -----------------------------------------------------------
# 📘 Approach 3: Sort by Frequency (Not optimal)
# Sort items by frequency descending and return top k.
# Time: O(n log n)
# Space: O(n)
# -----------------------------------------------------------

class SolutionSort:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        for num in nums:
            freqMap[num] += 1

        # Sort by frequency descending
        sortedItems = sorted(freqMap.items(), key=lambda x: x[1], reverse=True)

        # Return top k elements
        return [item[0] for item in sortedItems[:k]]