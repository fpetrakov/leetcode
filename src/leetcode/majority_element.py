from collections import defaultdict
from typing import list


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counter = defaultdict(int)
        val = 0
        key = nums[0]

        for num in nums:
            counter[num] += 1
            if counter[num] > val:
                val = counter[num]
                key = num

        return key
