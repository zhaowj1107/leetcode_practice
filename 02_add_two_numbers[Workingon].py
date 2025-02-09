"""
Do not know what the ListNode is
Working on it
2025/02/07
"""
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        curr1 = l1
        curr2 = l2
        list1 = []
        list2 = []
        while curr1:
            list1.append(curr1.val)
            curr1 = curr1.next
        while curr2:
            list2.append(curr2.val)
            curr2 = curr2.next
        list1 = list1[::-1]
        list2 = list2[::-1]
        for x in range(len(list1)):
            num1 += list1[x]*10**(len(list1) - x - 1)
        for x in range(len(list2)):
            num2 += list2[x]*10**(len(list2) - x - 1)
        
        num3 = num1 + num2
        list3 = list(str(num3))

        l3 = ListNode(0)

        for value in list3:
            l3.next = ListNode(value)
            l3 = l3.next

        return l3

