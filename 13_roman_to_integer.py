"""
Time complexity: Beat 48%
Memory complexity: Beat 18%
2025/02/06
"""
def romanToInt(s: str):
    integer = 0
    while s != '':
        if s[0] == 'M':
            integer += 1000
            s = s[1:]
        elif s[0:2] == 'CM':
            integer += 900
            s = s[2:]
        elif s[0] == "D":
            integer += 500
            s = s[1:]
        elif s[0:2] == "CD":
            integer += 400
            s = s[2:]
        elif s[0] == "C":
            integer += 100
            s = s[1:]
        elif s[0:2] == "XC":
            integer += 90
            s = s[2:]
        elif s[0] == "L":
            integer += 50
            s = s[1:]
        elif s[0:2] == "XL":
            integer += 40
            s = s[2:]
        elif s[0] == "X":
            integer += 10
            s = s[1:]
        elif s[0:2] == "IX":
            integer += 9
            s = s[2:]
        elif s[0] == "V":
            integer += 5
            s = s[1:]
        elif s[0:2] == "IV":
            integer += 4
            s = s[2:]
        elif s[0] == "I":
            integer += 1
            s = s[1:]
    return integer

print(romanToInt("III"))