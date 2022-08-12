def isPalindrome_wiht_convertion_to_string(x: int) -> bool:
    x = str(x)
    return True if (x == x[::-1]) else False
