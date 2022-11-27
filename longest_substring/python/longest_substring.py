class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_lengh = 0
        uniq = set()
        for ch in s:
            if ch not in uniq:
                uniq.add(ch)
            else:
                if len(uniq) > max_lengh:
                    max_lengh = len(uniq)
                uniq = set()
                uniq.add(ch)
        return max_lengh


