def plusOne(digits: list) -> int:
    digits = [str(x) for x in digits]
    digits = "".join(digits)
    number = ''
    for i in digits:
        number += i
    number = int(number) + 1
    number = str(number)
    number = [int(i) for i in number]
    return number