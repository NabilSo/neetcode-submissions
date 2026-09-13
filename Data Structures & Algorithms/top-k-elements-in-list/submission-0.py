from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # most_common(k) returns a list of tuples: e.g., [(7, 2)]
        # Use a list comprehension to extract just the keys
        return [num for num, count in Counter(nums).most_common(k)]