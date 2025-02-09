def longestCommonPrefix(strs) -> str:
    if len(strs) == 0 or strs[0] == '':
        return ""
    
    max_letter_length = 200
    for str in strs:
        if len(str) < max_letter_length:
            max_letter_length = len(str)
    """
    cp = strs[0][0]
    for str_index in range(0,len(strs)):
        for letter_index in range(max_letter_length):
            if strs[str_index][letter_index]
    """
    loop_control = True
    while loop_control:
        cp = strs[0][0:max_letter_length]
        counter = 0
        for str in strs:
            if str[0:max_letter_length] != cp:
                break
            else:
                counter += 1
        if counter == len(strs):
            return cp
        max_letter_length -= 1
    
    return ""

print(longestCommonPrefix(["flower","flow","flight"]))