"""
Time complexity: Beat 31%
Memory complexity: Beat 33%
2025/02/08
"""

def reverse(x: int) -> int:
    if x < 0:
        reverse_x = str(x).replace("-","")[::-1]
        new_x = (int(reverse_x))
        new_x = new_x*(-1)
    else:
        reverse_x = str(x).replace("-","")[::-1]
        new_x = int(reverse_x)
    
    if new_x > 2**31 - 1 or new_x < -2**31:
        return 0
    else:
        return new_x

print(reverse(-321))