def prefix(strs: list[str]) -> str:
    l = ''
    l += strs[0][0]
    l += strs[0][1]
    flag = 0
    for word in strs:
        for i in range(len(word)):
            if word[i] == l[0] and word[i + 1] == l[1]:
                flag += 1

    if flag == 3:
        return l


user_input = input()
if __name__ == "__main__":
    prefix(user_input)