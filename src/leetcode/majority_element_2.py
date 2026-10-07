from collections import Counter
from typing import list


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count = Counter(nums)

        l = len(nums)
        result = []
        for key, value in count.items():
            if value > (l / 3):
                result.append(key)

        return result
