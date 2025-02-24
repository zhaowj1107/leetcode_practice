def isValid(s: str) -> bool:
    # 想法太复杂了，去消除s中的三组括号，消到不能消就返回Flase
    answer1 = "()"
    answer2 = '[]'
    answer3 = "{}"
    index = 0
    if len(s) % 2 == 1:
        return False
    while len(s) > 0:
        if s[index] + s[len(s) - index - 1] == answer1 or s[index] + s[len(s) - index - 1] == answer2 or s[index] + s[len(s) - index - 1] == answer3:
            s = s[index + 1: len(s) - index - 1]
            continue
        for symbol in range(len(s)):
            for symbol_pair in range(symbol + 1, len(s)):
                if s[symbol] + s[symbol_pair] == answer1 or s[symbol] + s[symbol_pair] == answer2 or s[symbol] + s[symbol_pair] == answer3:
                    if (symbol_pair - symbol) % 2 == 0:
                        return False
                    else:
                        s = s[:symbol_pair] + s[symbol_pair+1:]
                        s = s[:symbol] + s[symbol+1:]
                        break
                else:
                    if len(s) == 2:
                        return False
            break
    return True

print(isValid("[([]])"))