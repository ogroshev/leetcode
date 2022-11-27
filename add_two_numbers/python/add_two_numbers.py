from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toPyList(self):
        res = []
        while True:
            res.append(self.val)
            self = self.next
            if self == None:
                break
        return res

    # def  fromNumber(self, number):


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        firstNode = ListNode(next=None)
        prevNode = ListNode(next=None)
        currNode = ListNode(next=None)
        isFirst = True
        transfer = 0
        while l1 != None or l2 != None or transfer != 0:
            val1 = self.__getValue(l1)
            val2 = self.__getValue(l2)
            
            sum = val1+val2 + transfer
            if sum >= 10:
                value = sum - 10
                transfer = 1
            else:
                value = sum
                transfer = 0
            
            if isFirst:
                firstNode.val = value
                firstNode.next = currNode
                prevNode = firstNode
                isFirst = False
            else:
                nextNode = ListNode(next=None)
                currNode.val = value
                currNode.next = nextNode
                prevNode = currNode
                currNode = nextNode
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        prevNode.next = None
        return firstNode
    
    def __getValue(self, l: Optional[ListNode]):
        if l:
            val = l.val
        else:
            val = 0
        return val

