

def romanToInt(s: str) -> int:
    summary = 0
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "temp": 0}
    length = len(s) - 1
    index = 0
    while index != len(s):
        if index != length and s[index] == 'I' and (s[index + 1] == 'V' or s[index + 1] == 'X'):
            summary += values[s[index + 1]] - values[s[index]]
            index += 1
        elif index != length and s[index] == 'X' and (s[index + 1] == 'L' or s[index + 1] == 'C'):
            summary += values[s[index + 1]] - values[s[index]]
            index += 1
        elif index != length and s[index] == 'C' and (s[index + 1] == 'D' or s[index + 1] == 'M'):
            summary += values[s[index + 1]] - values[s[index]]
            index += 1

        else:
            summary += values[s[index]]
        index += 1

    return summary


user_input = input()
if __name__ == "__main__":
    print(romanToInt(user_input))