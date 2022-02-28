#!/usr/bin/env python3

from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Very verbose, suffers from DRY, needs refactor.
        Runtime: 84ms
        '''

        l3 = ListNode()
        start = l3

        while l1 and l2:
            if l1.val + l2.val + l3.val >= 10:
                l3.next = ListNode(1)

            l3.val = (l1.val + l2.val + l3.val) % 10

            if l1.next or l2.next:
                if l3.next:
                    l3 = l3.next
                else:
                    l3.next = ListNode()
                    l3 = l3.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            l3.val += l1.val

            if l3.val == 10:
                l3.val = 0
                l3.next = ListNode(1)
                l3 = l3.next
                l1 = l1.next
            elif l1.next:
                l3.next = ListNode()
                l3 = l3.next
                l1 = l1.next
            else:
                l1 = l1.next

        while l2:
            l3.val += l2.val

            if l3.val == 10:
                l3.val = 0
                l3.next = ListNode(1)
                l3 = l3.next
                l2 = l2.next
            elif l2.next:
                l3.next = ListNode()
                l3 = l3.next
                l2 = l2.next
            else:
                l2 = l2.next

        return start
