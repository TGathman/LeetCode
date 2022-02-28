#!/usr/bin/env python3

class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        Original, naive solution
        Runtime 5960 ms
        '''
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        Using a hash map.
        Runtime 97 ms
        '''

        complements = {}

        for idx, ele in enumerate(nums):
            comp = target - ele
            if comp in complements:
                return [idx, complements[comp]]
            complements[ele] = idx
