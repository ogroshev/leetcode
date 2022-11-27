import longest_substring
import unittest

class TestSolution(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        self.assertEqual(longest_substring.Solution.lengthOfLongestSubstring(self, s="abcabcbb"), 3)
        self.assertEqual(longest_substring.Solution.lengthOfLongestSubstring(self, s="bbbbb"), 1)
        self.assertEqual(longest_substring.Solution.lengthOfLongestSubstring(self, s="pwwkew"), 3)


if __name__ == '__main__':
    unittest.main()