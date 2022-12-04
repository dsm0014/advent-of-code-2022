from typing import List
import string


def solve1(lines: List[str]) -> int:
    """
    bag split compartments grand total
    """
    ans = 0
    for line in lines:
        mid = int(len(line) / 2)
        c1, c2 = line[:mid], line[mid:]
        ans += next(string.ascii_uppercase.index(i) + 27 if i not in string.ascii_lowercase
                    else string.ascii_lowercase.index(i) + 1 for i in c1 if i in c2)
    return ans


def solve2(lines: List[str]) -> int:
    """
    common in compartments per 3 elves
    """
    ans = 0
    for i, line in enumerate(lines):
        if i % 3:
            continue
        ans += next(string.ascii_uppercase.index(j) + 27 if j not in string.ascii_lowercase
                    else string.ascii_lowercase.index(j) + 1 for j in line if j in lines[i + 1] and j in lines[i + 2])

    return ans


if __name__ == '__main__':
    lines = []
    with open('data.txt', 'r') as f:
        lines = [line for line in f.readlines()]
    print(solve1(lines))
    print(solve2(lines))
