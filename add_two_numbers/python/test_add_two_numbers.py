import add_two_numbers
import unittest

class TestSolution(unittest.TestCase):
    def test_toPyList(self):
        node = add_two_numbers.ListNode(1, None)
        node = add_two_numbers.ListNode(2, node)
        node = add_two_numbers.ListNode(3, node)
        self.assertEqual(node.toPyList(), [3,2,1])

    def test_addTwoNumbers(self):
        node = add_two_numbers.ListNode(3, None)
        node = add_two_numbers.ListNode(4, node)
        l1 = add_two_numbers.ListNode(2, node)

        node = add_two_numbers.ListNode(4, None)
        node = add_two_numbers.ListNode(6, node)
        l2 = add_two_numbers.ListNode(5, node)

        s = add_two_numbers.Solution()
        self.assertEqual(s.addTwoNumbers(l1, l2).toPyList(), [7,0,8])

        l1 = add_two_numbers.ListNode(0, None)
        l2 = add_two_numbers.ListNode(0, None)
        self.assertEqual(s.addTwoNumbers(l1, l2).toPyList(), [0])     
        

