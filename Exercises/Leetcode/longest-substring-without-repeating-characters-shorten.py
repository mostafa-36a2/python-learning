class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        longest_substr_len = 0
        substr_idx = 0

        for idx, c in enumerate(s):
            if c in d:
                substr_idx = max(substr_idx, d[c] + 1)

            longest_substr_len = max(longest_substr_len, idx - substr_idx + 1)

            # Save the last occurance
            d[c] = idx

        return longest_substr_len
