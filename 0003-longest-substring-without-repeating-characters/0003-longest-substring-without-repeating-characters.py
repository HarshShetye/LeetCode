class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest_substring = ""
        current_substring = ""
        for i in range(n):
            if s[i] not in current_substring:
                current_substring += s[i]
            else:
                if len(current_substring) > len(longest_substring):
                    longest_substring = current_substring
                current_substring = current_substring[current_substring.index(s[i]) + 1:] + s[i]
        return max(len(longest_substring), len(current_substring))

        