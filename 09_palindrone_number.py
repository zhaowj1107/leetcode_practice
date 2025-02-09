"""
Time complexity: Beat 72%
Memory complexity: Beat 56%
2025/02/06
"""

def isPalindrome(x: int):
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

print(isPalindrome('cbbd'))