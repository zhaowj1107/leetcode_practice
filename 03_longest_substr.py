"""
Time complexity: Beat 64%
Memory complexity: Beat 11%
The loookup efficienct between list and dict
2025/02/07
"""

def lengthOfLongestSubstring(s: str) -> int:
    switch = 1
    list_result = []
    if s == "":
        return 0
    longest_word = s[0]
    for index in range(1,len(s)):
        if s[index] == s[index - 1]:
            if switch == 0:
                pass
            else:
                switch = 0
                list_result.append(longest_word)
                longest_word = ''
        else:
            if switch == 0:
                longest_word = s[index-1] + s[index]
                switch = 1
            else:
                if s[index] in longest_word:
                    list_result.append(longest_word)
                    lon_word_index = longest_word.find(s[index])
                    longest_word = longest_word[lon_word_index+1:] + s[index]
                else:
                    longest_word += s[index]
                    switch = 1
    list_result.append(longest_word)
    lar_num = 0
    for word in list_result:
        if len(word) > lar_num:
            lar_num = len(word)
    return lar_num


print(lengthOfLongestSubstring("abcabcbb"))