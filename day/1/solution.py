from typing import List

def solve1(lines: List[str]) -> int:
    """
    Total calories in the food carried by elf with most food
    """
    ans = []
    tmp = 0
    for line in lines:
        if line != '\n':
            tmp += int(line)
            continue
        ans.append(tmp)
        tmp = 0

    return max(ans)


def solve2(lines: List[str]) -> int:
    """
    Total calories in the food carried by TOP THREE elves with most food
    """
    ans = []
    tmp = 0
    for line in lines:
        if line != '\n':
            tmp += int(line)
            continue
        ans.append(tmp)
        tmp = 0
        while len(ans) > 3:
            ans.remove(min(ans))

    return sum(ans)


if __name__ == '__main__':
    lines = []
    with open('data.txt', 'r') as f:
        lines = [line for line in f.readlines()]
    print(solve1(lines))
    print(solve2(lines))
