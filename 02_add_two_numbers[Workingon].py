"""
Do not know what the ListNode is
Working on it
2025/02/07
"""

def addTwoNumbers(l1: list, l2: list) -> list: # solve this with list
        num1 = 0
        num2 = 0
        list1 = l1[::-1]
        list2 = l2[::-1]
        for x in range(len(list1)):
            num1 += list1[x]*10**(len(list1) - x - 1)
        for x in range(len(list2)):
            num2 += list2[x]*10**(len(list2) - x - 1)
        
        num3 = num1 + num2
        list3 = list(str(num3))

        return list3[::-1]

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

print(addTwoNumbers(l1, l2))

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        total = carry = 0

        while l1 or l2 or carry:
            total = carry
            
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next

        return res.next

"""