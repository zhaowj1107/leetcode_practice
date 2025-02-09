"""
Time complexity: Beat 17%
Memory complexity: Beat 6%
2025/02/07
Need to improve
https://leetcode.com/problems/longest-palindromic-substring/solutions/4212564/beats-96-49-5-different-approaches-brute-force-eac-dp-ma-recursion
"""

def longestPalindrome(s: str) -> str:
    result = []
    reverse_s = s[::-1]
    length = len(s)
    for forward_word in range(length):
        for backward_word in range(length):
            if s[forward_word] == reverse_s[backward_word]:
                if s[forward_word:length - backward_word] == reverse_s[backward_word:length - forward_word]:
                    result.append(s[forward_word:length - backward_word])

    lar_num = 0
    lar_subs = ''
    for word in result:
        if len(word) > lar_num:
            lar_num = len(word)
            lar_subs = word
    return lar_subs


print(longestPalindrome("aabcba"))