def solve1(file) -> int:
    """
    Total calories in the food carried by elf with most food
    """
    ans = []
    tmp = 0
    for line in file.readlines():
        if line != '\n':
            tmp += int(line)
            continue
        ans.append(tmp)
        tmp = 0

    return max(ans)


def solve2(file) -> int:
    """
    Total calories in the food carried by TOP THREE elves with most food
    """
    ans = []
    tmp = 0
    for line in file.readlines():
        if line != '\n':
            tmp += int(line)
            continue
        ans.append(tmp)
        tmp = 0
        while len(ans) > 3:
            ans.remove(min(ans))

    return sum(ans)


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        print(solve1(f))

    with open('data.txt', 'r') as f:
        print(solve2(f))
