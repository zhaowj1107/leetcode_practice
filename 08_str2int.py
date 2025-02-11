"""
Time complexity: Beat 39%
Memory complexity: Beat 28%
2025/02/11
"""

def myAtoi(s: str) -> int:
    s = s.strip()
    if s == "":
        return 0
    CONSTANT = ["0","1","2","3","4","5","6","7","8","9","0"]
    signedness = 0
    if s[0] == "-":
        signedness = -1
        s = s[1:]
    elif s[0] == "+":
        signedness = 1
        s = s[1:]
    else:
        signedness = 1
    new_str = []
    for letter in s:
        if letter in CONSTANT:
            new_str.append(letter)
        else:
            break
    if new_str == []:
        # print(0)
        return 0
    result = ''.join(new_str)
    
    result = int(result) * signedness

    if result > 2**31 -1:
        return 2**31 - 1
    elif result< -(2**31):
        return -(2**31)
    else:
    # print(result)
        return result

myAtoi("-91283472332")   