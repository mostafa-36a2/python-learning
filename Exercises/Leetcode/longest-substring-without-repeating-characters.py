debug = False


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary of character
        # -> last occurance index, index_of_substring
        d = dict()
        index_of_longest_substring = 0
        longest_substring_length = 0
        curr_first_index_of_substring = 0

        for index, character in enumerate(s):
            if debug:
                print(f"----> parsing reached {s[:index+1]}")
            if character in d:
                # Only if index is bigger than curr_first_index_of_substring
                if d[character][0] >= curr_first_index_of_substring:
                    if debug:
                        print(f"character({character}) is in d, at {d[character][0]}")
                    curr_first_index_of_substring = d[character][0] + 1
                    d[character] = (index, curr_first_index_of_substring + 1)
                else:
                    # If index is older, just ignore it as if it didn't occure before
                    pass

            d[character] = (index, curr_first_index_of_substring)
            substring_length = index - curr_first_index_of_substring + 1

            if substring_length > longest_substring_length:
                index_of_longest_substring = curr_first_index_of_substring
                longest_substring_length = substring_length
                if debug:
                    print(
                        f"New longest substring, index={index_of_longest_substring}, length={longest_substring_length}"
                    )

            if debug:
                print(
                    d,
                    s[
                        index_of_longest_substring : index_of_longest_substring
                        + longest_substring_length
                    ],
                )
        return longest_substring_length


# print(Solution().lengthOfLongestSubstring("abcdefjklmnop"))
# print(Solution().lengthOfLongestSubstring("abcaedfcjklbm"))
# print(Solution().lengthOfLongestSubstring("bbbbbbbb"))
# print(Solution().lengthOfLongestSubstring("aaaabbbb"))
if debug:
    # print(Solution().lengthOfLongestSubstring("tmmzuxt"))
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
