#!/usr/bin/env python3

from collections import deque


class Solution:

    def isPalindrome(self, x: int) -> bool:
        """
        Runtime: 108ms
        """

        return str(x) == str(x)[::-1]

    def isPalindrome(self, x: int) -> bool:
        """
        Solution without converting to string.
        Runtime: 82ms
        """
        if x < 0:
            return False

        backward = []
        forward = deque([])

        while x > 0:
            backward.append(x % 10)
            forward.appendleft(x % 10)
            x = x // 10

        for idx, ele in enumerate(backward):
            if ele != forward[idx]:
                return False

        return True