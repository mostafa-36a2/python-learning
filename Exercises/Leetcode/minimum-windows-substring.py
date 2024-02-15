from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_char_count = defaultdict(int)
        done_tracker = defaultdict(bool)
        # No need for order in t at all
        for c in t:
            t_char_count[c] += 1
            done_tracker[c] = False

        current_ = []
        leftmost_current_pointer = -1
        tracker = defaultdict(int)

        min_len = 9999999
        start_arr = -1
        end_arr = -1

        for i, c in enumerate(s):
            # Trigger point, character is in `t`
            if c in t_char_count:
                # Character included in the string
                tracker[c] += 1
                if tracker[c] >= t_char_count[c]:
                    if c in done_tracker:
                        del done_tracker[c]
                else:
                    done_tracker[c] = False
                current_.append((c, i))
                if leftmost_current_pointer == -1:
                    leftmost_current_pointer = 0
            # else Ignore any other character

            # Window is complete
            while len(done_tracker) == 0:
                # print(s[current_[0][1]:current_[-1][1]+1])
                len_str = current_[-1][1] - current_[leftmost_current_pointer][1] + 1
                if len_str < min_len:
                    min_len = len_str
                    start_arr = current_[leftmost_current_pointer][1]
                    end_arr = current_[-1][1] + 1

                # Pop the first
                c = current_[leftmost_current_pointer][0]
                i = current_[leftmost_current_pointer][1]
                tracker[c] -= 1
                if tracker[c] < t_char_count[c]:
                    done_tracker[c] = False
                leftmost_current_pointer += 1

        if start_arr == -1:
            return ""
        return "".join(s[start_arr:end_arr])
